from django.shortcuts import render,redirect
from .forms import UserCreationForm,Signup
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def home(request):
    detail=User.objects.all()
    return render(request,'home.html',{'detail':detail})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form= Signup(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')  
            user=authenticate(username=username,password=password)
            login(request,user)
            print(username,password)
            messages.success(request,"Your account is Created Successfully")
            return redirect('home')
        else:
            form=Signup()
            messages.error(request,"username and password are invalid,Please Try again")
            return render(request,'register.html',{'form':form})     
    else:
        form=Signup()
        return render(request,'register.html',{'form':form})
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(username,password)
            return redirect('home')
        else:
            messages.success(request, 'username and password are invalid,Please Try again')
            return render(request,'signin.html')    
    else:
        return render(request,'signin.html')
def signout(request):
    logout(request)
    return redirect('signin')