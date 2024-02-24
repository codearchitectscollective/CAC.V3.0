from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
import re
import logging
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from django.conf import settings
from CAC.settings import LOGIN_ATTEMPTS_LIMIT, LOGIN_ATTEMPTS_TIMEOUT
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request): 
    return render(request, 'blog.html')

def contact(request): 
    return render(request, 'contact.html')

def purchase(request):
    return render(request, 'purchase.html')

def timeline(request): 
    return render(request, 'timeline.html')

def arcade(request): 
    return render(request, 'arcade.html')

def payment(request): 
    return render(request, 'payment.html')

def colorpicker(request): 
    return render(request, 'colorpicker.html')

def loremgenerator(request): 
    return render(request, 'loremgenerator.html')

def tetris(request): 
    return render(request, 'tetris.html')

def snake(request): 
    return render(request, 'snake.html')

def paint(request): 
    return render(request, 'paint.html')

@login_required()
def password(request): 
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If Profile doesn't exist, create a new one it is used for admin and I am him so wasup?
        profile = Profile.objects.create(user=request.user, bio='', image='')  # Adjust bio and image as needed
    return render(request, 'password.html', {'profile': profile})

def pong(request): 
    return render(request, 'pong.html')

def signup(request): 
    return render(request, 'signup.html')

def mario(request): 
    return render(request, 'mario.html')

def login(request): 
    return render(request, 'login.html')

def googlemap(request): 
    return render(request, 'googlemap.html')

@login_required()
def forgetpass(request): 
    return render(request, 'forgetpass.html')

def blogmenu(request):
    context = {
        'posts' : Post.objects.all()
    } 
    return render(request, 'blogmenu.html', context)

def verification(request): 
    return render(request, 'verification.html')

@login_required()
def notepad(request): 
    return render(request, 'notepad.html')

@login_required()
def myip(request): 
    return render(request, 'myip.html')

@login_required()
def calculator(request): 
    return render(request, 'calculator.html')

def arcadegames(request): 
    return render(request, 'arcadegames.html')

@login_required()
def profile(request): 
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If Profile doesn't exist, create a new one it is used for admin and I am him so wasup?
        profile = Profile.objects.create(user=request.user, bio='', image='')  # Adjust bio and image as needed
    return render(request, 'profile.html', {'profile': profile})

@login_required()
def camera(request): 
    return render(request, 'camera.html')

@login_required()
def internetspeedtest(request): 
    return render(request, 'internetspeedtest.html')

@login_required()
def resetpassword(request): 
    return render(request, 'resetpassword.html')

@login_required()
def tools(request): 
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If Profile doesn't exist, create a new one it is used for admin and I am him so wasup?
        profile = Profile.objects.create(user=request.user, bio='', image='')  # Adjust bio and image as needed
    return render(request, 'tools.html', {'profile': profile})


@login_required()
def passwordgenerator(request): 
    return render(request, 'passwordgenerator.html')

@login_required()
def settings(request): 
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If Profile doesn't exist, create a new one it is used for admin and I am him so wasup?
        profile = Profile.objects.create(user=request.user, bio='', image='')  # Adjust bio and image as needed
    return render(request, 'settings.html', {'profile': profile})

def home(request):
    return redirect('/')

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog.html', {'post': post})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'update_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the user's session to reflect the password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Redirect to the user's profile page after password change
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

#function for register 
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            passwordre = request.POST.get('passwordre')
            
            # Check if any of the fields are empty
            if not (username and email and password and passwordre):
                messages.info(request, "Please provide all needed information.")
                return redirect('signup')
            
            # Validate email format
            if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                messages.info(request, "Please provide a valid email address.")
                return redirect('signup')

            # Check password length
            if len(password) < 6 or len(passwordre) < 6:
                messages.info(request, "Your password must be at least 6 characters.")
                return redirect('signup')
            
            # Check password complexity
            if not (
                re.search("[a-z]", password) and
                re.search("[A-Z]", password) and
                re.search("\d", password) and
                re.search("[$@!%*?&]", password)
                ):
                messages.info(request, "Your password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                return redirect('signup')
            
            # Check if passwords match
            if password != passwordre:
                messages.info(request, "Passwords do not match.")
                return redirect('signup')
            
            # Check for existing email and username
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use.")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use.")
                return redirect('signup')
            
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, f"Account Created for {user}")
            return redirect('login')
        else:
            return render(request, 'signup.html')
    except Exception as e:
        messages.info(request, f"An error occurred: {e}")
        return redirect('signup')
    
#function for login\
    
limit = LOGIN_ATTEMPTS_LIMIT
logger = logging.getLogger(__name__)

def login(request):
    try:
        next_url = request.GET.get('next', '/')  # Default to home page if 'next' parameter is not provided
        
        # If user is already authenticated, redirect to profile page
        if request.user.is_authenticated:
            return redirect('profile')

        if request.method == 'POST':
            ip_address = request.META.get('REMOTE_ADDR')
            login_attempts_key = f'login_attempts_{ip_address}'
            login_attempts = cache.get(login_attempts_key, 0)
            
            logger.info(f'Login attempt from IP: {ip_address}, Username: {request.POST.get("username")}')

            if login_attempts >= limit:
                messages.error(request, 'Too many login attempts. Please try again later.')
                return redirect('login')

            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    cache.delete(login_attempts_key)
                    logger.info(f'Successful login for user: {username}, IP: {ip_address}')

                    messages.success(request, 'You have successfully logged in.')
                    
                    next_url = request.POST.get('next')
                    if next_url:
                        return redirect(next_url)
                    else:
                        return redirect('profile')   # Redirect to the profile page if no next URL
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')

            cache.set(login_attempts_key, login_attempts + 1, timeout=LOGIN_ATTEMPTS_TIMEOUT)
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'next': next_url})
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        messages.error(request, 'An unexpected error occurred. Please try again later.')
        return redirect('login')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/')




#mrnone wrote this 
#django be acting like a miaatch 
