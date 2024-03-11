from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import CustomUser as User
from django.db import IntegrityError

def user_login(request):
    return render(request, "users/login.html")


def user_register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if cpassword != password:
            return redirect('register')
        try:
            user = User.objects.create(full_name=name, email=email, password=password)
        except IntegrityError:
            print("User exist already.")
            return redirect('register')
        login(request,user)
        return redirect('index')
    return render(request, "users/register.html")


def user_logout(request):
    logout(request)
