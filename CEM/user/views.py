from django.shortcuts import render
from .models import User


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


def dashboard(request):
    return render(request,'user/dashboard/dashboard.html')


    