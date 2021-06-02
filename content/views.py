from django.shortcuts import render,HttpResponse,Http404
import os
from django.conf import settings
from .models import course,course_reviews,tutorials,instructor
from dashboard.models import courses_enrolled


def contentView(request):
    var = {}
    for c in course.objects.all():
        ci = c.instructor_name
        for i in instructor.objects.all():
            if str(i.instructor_name) == str(ci):
                print(str(ci),i.instructor_name)
                var[c] = i
    return render(
    request = request,
    template_name='courses_new.html' ,
    context= {"var":var})

def single_slug(request,single_slug):
    courses = [i.course_slug for i in course.objects.all()]
    #print(courses)

    if single_slug in courses:
        current_tutorials = []
        for c in course.objects.all():
            if c.course_slug == single_slug:
                current_course = c.course_name
                instr = c.instructor_name
                course_details = c.course_info


        current_tutorials = []
        for t in tutorials.objects.all():
            print(current_course,t.course_name)
            if str(t.course_name) == str(current_course):
                print('true')
                current_tutorials.append(t)
        for i in instructor.objects.all():
            if i.instructor_name == instr:
                instructor_details = i
        #print('current course:',current_course)
        #print(current_tutorials)
        return render(request,'tut_display.html',context={'tuts':current_tutorials,'instructor':instr,'course':current_course,'course_details':course_details})

def detailed_single_slug(request,single_slug):
    courses = [i.course_slug for i in course.objects.all()]
    if single_slug in courses:
        current_tutorials = []
        for c in course.objects.all():
            if c.course_slug == single_slug:
                current_course = c.course_name
                instr = c.instructor_name
                course_det = c
        current_tutorials = []
        for t in tutorials.objects.all():
            print(current_course,t.course_name)
            if str(t.course_name) == str(current_course):
                print('true')
                current_tutorials.append(t)
        for i in instructor.objects.all():
            if i.instructor_name == instr:
                instructor_details = i   
    return render(request,'course_details.html',{'course':course_det,'ins':instructor_details})


def enroll_single_slug(request,single_slug):
    courses = [i.course_slug for i in course.objects.all()]
    #print(courses)



    if single_slug in courses:
        current_tutorials = []
        for c in course.objects.all():
            if c.course_slug == single_slug:
                current_course = c.course_name
                instr = c.instructor_name
                course_det = c
        current_tutorials = []
        for t in tutorials.objects.all():
            print(current_course,t.course_name)
            if str(t.course_name) == str(current_course):
                print('true')
                current_tutorials.append(t)
        for i in instructor.objects.all():
            if i.instructor_name == instr:
                instructor_details = i
        #print('current course:',current_course)
        #print(current_tutorials)
        current_user = request.user
        temp = courses_enrolled(username = current_user,course_name = course_det)
        temp.save()
        return render(request,'tutorials.html',context={'tuts':current_tutorials,'ins':instructor_details,'course':current_course})


def test(request):
    return render(request,'videodisp.html',context={'tuts':tutorials.objects.all()})