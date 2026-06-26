from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'index.html')
def logout_a(request):
    logout(request)
    return redirect('home')
def login_a(request):
    if request.method=='GET':
        return render(request,'loginacc.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'loginacc.html',{'form':AuthenticationForm(),'error':'wrong username or password'})
        else:
            login(request,user)
            return redirect('home')
def signup(request):
    if request.method=='GET':
        return render(request,'signupacc.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                redirect('home')
            except:
                return render(request,'signupacc.html',{'form':UserCreationForm,'error':'already exists'})
        else:
                return render(request,'signupacc.html',{'form':UserCreationForm,'error':'password doesnot match'})



