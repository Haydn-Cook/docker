from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def login_create(request):
    return render(request, ('login/login_or_create.html'))

def login(request):
    return render(request, ('login/login.html'))

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide a username and password')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists. Please use another.')
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'User account created successfully')
                return redirect('homepage:Homepage')  # Redirect to the login page after successful user creation

    return render(request, 'login/login.html')


