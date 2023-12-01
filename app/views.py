from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username']=user.username
            login(request, user,backend='app.auth_backends.CustomUserModelBackend')
            return redirect('home')  # replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def signin(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email)
            print(password)
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user,backend='app.auth_backends.CustomUserModelBackend')
                request.session['username']=user.username
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'app/signin.html', {'form': form})


def home(request):
    username=request.session.get('username')
    print(username)
    return render(request, 'app/home.html', {'username': username})

def logoutview(request):
    logout(request)
    return redirect('signin')
