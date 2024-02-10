from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as user_login,logout as user_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')


        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        # Check if username is unique
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'register.html')

        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('homepage')
        
    return render(request, 'login.html')


@login_required(login_url='homepage')
def homepage(request):
    return render(request, 'homepage.html')
def logout(request):
    user_logout(request)
    redirect('login/')