from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Pass the username to the template context
        username = request.user.username
    else:
        username = None  # If user is not authenticated, set username to None

    return render(request, 'home.html', {'username': username})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')  # Redirect to register page if username exists
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.is_staff = True
                user.save()
                print("Registered successfully")
                return redirect('login_user')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')  # Redirect to register page if passwords do not match
    else:
        return render(request, "register.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login_user')  # Redirect to login page if authentication fails
    else:
        return render(request, "login.html")
    
def logout_user(request):
    auth.logout(request)
    return redirect('home')  # Redirect to home page after logout

def anime(request):
    return render(request, 'anime.html')

def scifi(request):
    return render(request, 'scifi.html')

def fantasy(request):
    return render(request, 'fantasy.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
