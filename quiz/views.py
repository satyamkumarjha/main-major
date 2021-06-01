from django.shortcuts import render
from .models import quiz,question
from content.models import course
from dashboard.models import quiz_scores

# Create your views here.

def dispTest(request,single_slug):
    #if request.method == "POST":
    #    print('true')
    #if request.method == "POST":
    for q in quiz.objects.all():
        if q.quiz_slug == single_slug:
            q_obj = q
    title = q_obj.quiz_name
    slug = q_obj.quiz_slug
    questions = []
    for q in question.objects.all():
        if q.course_name == q_obj.course_name:
            #print('true')
            if q.quiz_name == q_obj:
                questions.append(q)
    #print(questions)
    #print(title)
    return render(request,'test.html',{'question':questions,'title':title,'single_slug':slug})

def result(request,single_slug):
    #print(request.POST)
    #print(request.POST[str(1)])
    for q in quiz.objects.all():
        if q.quiz_slug == single_slug:
            q_obj = q
    for c in course.objects.all():
        if q_obj.course_name == c:
            print('c trye')
            c_obj = c
    current_user = request.user
    total = 0
    val = 1
    for q in question.objects.all():
        try:
            if request.POST[str(val)] == q.answer:
                total+=1
            val+=1
        except:
            pass
    temp = quiz_scores(username = current_user, course_name = c_obj, quiz_name = q_obj,score = total)
    temp.save()
    return render(request,'score.html',{'total':total})
