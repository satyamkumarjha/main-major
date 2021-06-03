from django.shortcuts import render
from content.models import instructor,course

# Create your views here.

def teacherView(request):
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    course_list = [[] for i in range(instructor.objects.count())]
    counter = 1
    for i in instructor.objects.all():
        for c in course.objects.all():
            if c.instructor_name == i.instructor_name:
                course_list[counter].append(c.course_name)
        counter+=1
    return render(request,'teachers.html',{'inst':instructor.objects.all(),'courses':course_list,'log':loggen_in, 'u':request.user})