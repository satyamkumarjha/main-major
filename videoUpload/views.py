from content.models import course
from django.contrib.auth.models import User
from django.shortcuts import render

def trial(request): 
    return render(request,'timepass.html',context={'tuts':course.objects.all(),'user':User.objects.all()})