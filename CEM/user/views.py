from django.shortcuts import render
from .models import User


# Create your views here.
def login(request):
    return render(request,'user/login.html')



def signup(request):
    res={}
    if request.method=='POST':
        username=request.POST['userName']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        print(request.POST)
        obj=User.objects.create(name=username,email=email,phone=phone,password=password)
        obj.save()
        print("User created successfully")
        res['status']="Account created successfully."
        return render(request,'user/signup.html',res)
    return render(request,'user/signup.html')
    