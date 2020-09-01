from django.shortcuts import render,redirect
#from .models import Forms
from django.contrib import messages
from django.contrib.auth.models import User,auth

def home(request):
    return render(request,'login.html')


def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #form=Forms(username, password)
        #user = authenticate(form)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            print("logged In")
            return redirect("/")
        else:
            print("invalid credentials")
            #messages.info(request,'invalid')
            return redirect('/register')

    else:
        return render(request,'register.html')


def register(request):

    if request.method=='POST':

        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=name).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user=User.objects.create_user(username=name,email=email,password=password1)
                user.save()
                print("user created")
        else:
            print("password not matching")
        return redirect('/login')
    else:
        return render(request,'register.html')


