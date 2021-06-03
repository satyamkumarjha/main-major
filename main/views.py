from django.shortcuts import render
from content.models import course_reviews

# Create your views here.

def homepage(request):
    print(request.user)
    print(request.user.is_authenticated)
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    rev = []
    for r in course_reviews.objects.all():
        if r != course_reviews.objects.first():
            rev.append(r)
    return render(request,'home_new_new.html',context={'rev':rev,'start':course_reviews.objects.first(),'log':loggen_in, 'u':request.user})

def contact(request):
    return render(request,'contact.html')