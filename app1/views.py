from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse('Passwords do not match')
        else:
            my_user=User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')
        # return HttpResponse('User created!')
        # print(username,email,password1,password2)
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')
        # print(username, password)
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def check_email_exists(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        user_exists = User.objects.filter(email=email).exists()

        if user_exists:
            return redirect('reset_password')
        else:
            return HttpResponse("Email does not exist!")
    return render(request, 'check_email_exists.html')
