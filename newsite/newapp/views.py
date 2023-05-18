from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'newapp/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        email = request.POST['email']
        
        password = request.POST['password']
        
        cpassword = request.POST['cpassword']
        if password != cpassword:
            return render(request, 'newapp/signup.html', {'error': 'Passwords do not match.'})
        
        # Check if a user with the provided username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'newapp/signup.html', {'error': 'Username already exists.'})
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        
        # Automatically log in the user after signup
        login(request, user)
        
        return redirect('login_user')  # Replace 'home' with the name of your homepage URL
    
    return render(request, 'newapp/signup.html')
        
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('index')  # Replace 'home' with the name of your homepage URL
        else:
            # Invalid credentials
            return render(request, 'newapp/login.html', {'error': 'Invalid username or password.'})
    
    return render(request, 'newapp/login.html')
    
def logout_view(request):
    request.session.flush()  # Clear all session data
      # Logout the user
    return render(request,'newapp/logout.html')

