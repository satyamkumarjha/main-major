from django.shortcuts import render
from content.models import instructor,course

# Create your views here.

def teacherView(request):
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    course_list = []
    course_list.append([])
    for i in instructor.objects.all():
        new_list = []
        for c in course.objects.all():
            if c.instructor_name == i.instructor_name:
                new_list.append(c.course_name)
        course_list.append(new_list)
    return render(request,'teachers.html',{'inst':instructor.objects.all(),'courses':course_list,'log':loggen_in, 'u':request.user})