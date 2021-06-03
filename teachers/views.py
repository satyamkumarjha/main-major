from django.shortcuts import render
from content.models import instructor,course

# Create your views here.

def teacherView(request):
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    teacher_dict = {}
    for i in instructor.objects.all():
        new_list = []
        for c in course.objects.all():
            if c.instructor_name == i.instructor_name:
                new_list.append(c.course_name)
        teacher_dict[i] = new_list
    return render(request,'instructors_new.html',{'inst':teacher_dict.items(),'log':loggen_in, 'u':request.user})