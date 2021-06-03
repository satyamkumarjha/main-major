from typing import Mapping
from django.shortcuts import render
from .models import student_details,courses_enrolled
from quiz.models import quiz
from content.models import course

# Create your views here.

def view_dashboard(request):
    loggen_in = False
    if request.user.is_authenticated:
        loggen_in = True
    current_user = request.user
    print(current_user)
    enrolled = []
    quizes = []
    main_map = {}
    course_map = {}
    for course in courses_enrolled.objects.all():
        if course.username == current_user:
            enrolled.append(course)
    for q in quiz.objects.all():
        print(q.course_name)
        for e in enrolled:
            if e.course_name == q.course_name:
                main_map[q] = e
                print('true')
                quizes.append(q)
    for student in student_details.objects.all():
        if student.username == current_user:
            target_student = student
    for c in enrolled:
        for t in course.objects.all():
            if c.course_name == t.course_name:
                course_map[c] = t.course_slug

    return render(request,'student-dashboard.html',{'student':target_student,'map':main_map.items(),'courses':course_map.items(), 'log':loggen_in, 'u':request.user})

#'courses':enrolled, 'quizes' : quizes