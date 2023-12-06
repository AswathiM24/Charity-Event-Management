from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User, Organization, Events ,Tickets
from .decorator import useronly
from django.core.mail import send_mail
from organisations.models import Login, UserInfo
import random


def generate_password():
    password = ''
    for i in range(12):
        password += chr(random.randint(33, 126))
    return password


# Create your views here.
def get_user(request):
    return User.objects.get(id=request.session['userid'])


def login(request):
    res = {}
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['passWord']
        print(request.POST)
        try:
            obj = User.objects.get(email=email, password=password)
            print("Login success")
            print(obj)
            res['status'] = 'Login success'
            request.session['userid'] = obj.id
            return redirect('user_dashboard')


        except Exception as e:
            print('Login failed')
            res['status'] = 'Login failed'
            res['code'] = 401  # not authenticated
            return render(request, 'user/login.html', res)

    return render(request, 'user/login.html')


def signup(request):
    res = {}
    if request.method == 'POST':
        username = request.POST['userName']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        print(request.POST)
        # obj=User()
        # obj.email=email
        # obj.name=username
        # obj.phone=phone
        # obj.password=password
        try:
            obj = User.objects.create(name=username, email=email, phone=phone, password=password)
            obj.save()
            print("User created successfully")
            res['status'] = "Account created successfully."
            return render(request, 'user/signup.html', res)
        except Exception as e:
            if 'UNIQUE constraint failed' in str(e):
                res['status'] = 'Already registered'
            else:
                res['status'] = e
            return render(request, 'user/signup.html', res)
    return render(request, 'user/signup.html')


@useronly
def dashboard(request):
    return render(request, 'user/dashboard/dashboard.html', {'user': get_user(request)})


@useronly
def organization(request):
    context = {}
    context['user'] = get_user(request)
    context['active'] = 'organisation_list'
    context['main_page'] = 'Organisation'
    context['sub_page'] = 'Organisation Lists'
    context['organizations'] = Organization.objects.all()
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        if id == '-1':
            obj = Organization()
        else:
            obj = Organization.objects.get(id=id)
        obj.name = request.POST['name']
        obj.address = request.POST['address']
        obj.phone = request.POST['phone']
        obj.email = request.POST['email']
        obj.fund_raised = request.POST['fund_raised']
        obj.status = True if 'status' in request.POST.keys() else False
        obj.save()
    return render(request, 'user/dashboard/Organisation_list.html', context)


# {
#   organization' : [
#                    {
#                       'id' :1,
#                       'name' :'Test Organization',
#                       'phone' :'987654321',
#                       'email' :'testOrgEmail@gmail.com',
#                       'address' :'Test Location',
#                       'status' :False,
#                       'fund_raised' :'0',
#                    },
#                    {
#                       'id' :2,
#                       'name' :'Test Organization',
#                       'phone' :'987654321',
#                       'email' :'testOrgEmail@gmail.com',
#                       'address' :'Test Location',
#                       'status' :False,
#                       'fund_raised' :'0',
#                    }
#                  ]
# }


@useronly
def logout(request):
    request.session.flush()
    return redirect('user_login')


def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('Email')

        try:
            obj = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)

        obj.password = generate_password()
        obj.save()

        send_mail(
            'Password Reset',
            f'Your password has been reset to: {obj.password}',
            'projectmail242@gmail.com',
            [email],
            fail_silently=False
        )

        return JsonResponse({'success': 'Password reset successfully'}, status=200)


@useronly
def show_all_events(request):
    context = {}
    context['user'] = get_user(request)
    context['active'] = 'events_list'
    context['main_page'] = 'Events'
    context['sub_page'] = 'Events Lists'
    context['events'] = Events.objects.all()

    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        if id == '-1':
            obj = Events()
        else:
            obj = Events.objects.get(id=id)
        obj.Name = request.POST['event_name']
        obj.org_email = request.POST['org_email']
        obj.org_name = request.POST['org_name']
        obj.org_phone = request.POST['org_phone']
        obj.description = request.POST['description']
        obj.location = request.POST['location']
        obj.ticket_price = request.POST['price']
        obj.date = request.POST['event_date']
        obj.organization = request.POST['hosted']
        obj.is_active = True if 'status' in request.POST.keys() else False
        obj.is_booking = True if 'is_booking' in request.POST.keys() else False
        obj.save()

    return render(request, 'user/dashboard/Events_list.html', context)


@useronly
def show_organizations_users(request):
    context = {}
    context['user'] = get_user(request)
    context['active'] = 'organisation_users_list'
    context['main_page'] = 'Organisation'
    context['sub_page'] = 'Staff Management'
    context['organisation'] = Organization.objects.all()
    context['users'] = UserInfo.objects.all()
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        if id == '-1':
            user_obj = UserInfo()
            login_obj = Login()
        else:
            user_obj = UserInfo.objects.get(id=id)
            login_obj = Login.objects.get(id=user_obj.auth.id)

        organisation = Organization.objects.get(id=request.POST['orgs'])

        login_obj.email = request.POST['email']
        if request.POST['password'] != '':
            login_obj.password = request.POST['password']
        login_obj.status = True if 'status' in request.POST.keys() else False
        login_obj.organization = organisation
        login_obj.save()

        user_obj.name = request.POST['name']
        user_obj.email = request.POST['email']
        user_obj.phone = request.POST['phone']
        user_obj.organization = organisation
        user_obj.auth = Login.objects.get(email=request.POST['email'])
        user_obj.is_staff = True if 'volunteer' in request.POST.keys() else False
        user_obj.is_active = True if 'status' in request.POST.keys() else False
        user_obj.is_admin = True if 'admin' in request.POST.keys() else False

        user_obj.save()

    return render(request, 'user/dashboard/orgs_users.html', context)


def show_tickets(request):
    context = {}
    context['user'] = get_user(request)
    context['active'] = 'ticket_list'
    context['main_page'] = 'Tickets'
    context['sub_page'] = 'Tickets'
    context['tickets'] = Tickets.objects.all()
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        obj = Tickets.objects.get(id=id)
        obj.action = request.POST.get('action')
        obj.closed_date = request.POST.get('close_date')
        obj.is_active = True if 'status' in request.POST.keys() else False
        obj.save()
    return render(request, 'user/dashboard/tickets.html',context)