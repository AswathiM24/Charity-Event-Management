from django.shortcuts import render
from .models import User,Organization
from .decorator import useronly

# Create your views here.

def login(request):
    res={}
    if request.method=='POST':
        email=request.POST['Email']
        password=request.POST['passWord']
        print(request.POST)
        try:
            obj=User.objects.get(email=email,password=password)
            print("Login success")
            print(obj)
            res['status']='Login success'
            request.session['userid'] = obj.id
            return render(request,'user/login.html',res)

            
        except Exception as e:
            print('Login failed')
            res['status']='Login failed'
            return render(request,'user/login.html',res)

    return render(request,'user/login.html')





def signup(request):
    res={}
    if request.method=='POST':
        username=request.POST['userName']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        print(request.POST)
        # obj=User()
        # obj.email=email
        # obj.name=username
        # obj.phone=phone
        # obj.password=password
        try:
            obj=User.objects.create(name=username,email=email,phone=phone,password=password)
            obj.save()
            print("User created successfully")
            res['status']="Account created successfully."
            return render(request,'user/signup.html',res)
        except Exception as e:
            if 'UNIQUE constraint failed' in str(e):
                res['status']='Already registered'
            else:
                res['status']=e
            return render(request,'user/signup.html',res)
    return render(request,'user/signup.html')


@useronly
def dashboard(request):
    logged_user = User.objects.get(id=request.session['userid'])
    return render(request,'user/dashboard/dashboard.html',{'user':logged_user})


    

def organization(request):
    context={}
    context['active'] ='organisation_list'
    context['main_page'] = 'Organisation'
    context['sub_page'] = 'Organisation Lists'
    context['organizations'] = Organization.objects.all()
    return render(request,'user/dashboard/Organisation_list.html',context)

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