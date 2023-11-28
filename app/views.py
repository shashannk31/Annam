from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            print("helooooooo")
        form = LoginForm()
    return render(request, 'app/signin.html', {'form': form})

def home(request):
    return render(request, 'app/home.html')
