from django.shortcuts import render

# Create your views here.

def teacherView(request):
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    return render(request,'teachers.html',{'log':loggen_in, 'u':request.user})