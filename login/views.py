from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .loginForm import LoginForm
from .registerForm import RegisterForm
from django.contrib import messages
from dashboard.models import student_details
from django.contrib.auth.models import User
from content.models import course_reviews
# Create your views here.



def login_request(request):
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                messages.info(request,f"You are now logged in as {username}")
                return redirect('/dashboard/')
            else:
                messages.error(request,"Invalid Username or Password")
        else:
            messages.error(request,"Invalid Username or Password")
    form = LoginForm
    return render(request,"login_form_new.html",context={"form":form})

def register_student(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created: {username}")
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            #user = User.objects.get(username=username)
            temp = student_details(username=user)
            temp.save()
            print(temp.username)
            return redirect('/dashboard/')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: form.error_messages[msg]")
    form = RegisterForm
    return render(request,"signup_form_new.html",context={"form":form})

def register_teacher(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created: {username}")
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard.view_dashboard')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: form.error_messages[msg]")
    form = RegisterForm
    return render(request,"register-teacher.html",context={"form":form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created: {username}")
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard.view_dashboard')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: form.error_messages[msg]")
    form = RegisterForm

    return render(request,"register.html",context={"form":form})

#def register_teacher(request):
 #   if request.method == "POST":
 #       form = RegisterForm(request.POST)
 #       if form.is_valid():
 #           user = form.save()
 #           user.group = 
 #           username = form.cleaned_data.get('username')
 #           messages.success(request,f"New Account Created: {username}")
 #           login(request,user,backend='django.contrib.auth.backends.ModelBackend')
 #           return redirect('main:homepage')
 #       else:
 #           for msg in form.error_messages:
 #               messages.error(request,f"{msg}: form.error_messages[msg]")
 #   form = RegisterForm
 #   return render(request,"register.html",context={"form":form})

def googleLogin(request):
    return render(request, "googleLogin.html")

def signout(request):
    logout(request)
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    rev = []
    for r in course_reviews.objects.all():
        if r != course_reviews.objects.first():
            rev.append(r)
    return render(request,'home_new.html',context={'rev':rev,'start':course_reviews.objects.first(),'log':loggen_in, 'u':request.user})