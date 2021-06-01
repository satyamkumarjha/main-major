from django.shortcuts import render

# Create your views here.

def teacherView(request):
    return render(request,'teachers.html')