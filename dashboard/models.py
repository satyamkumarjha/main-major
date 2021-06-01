from django.db import models
from quiz.models import quiz
from content.models import course
from django.contrib.auth.models import User

# Create your models here.

class student_details(models.Model):
    username = models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    dob = models.DateField(null=True)
    name = models.CharField(null=True,max_length=300)
    college = models.CharField(max_length=300,null=True)
    branch = models.CharField(max_length=300,null=True)
    email = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=11,null=True)
    photo = models.ImageField(blank = True,null=True)
    courses = models.TextField(null=True,blank=True)

class quiz_scores(models.Model):
    username = models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    course_name = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)
    quiz_name = models.ForeignKey(quiz,default=1,on_delete=models.SET_DEFAULT)
    score = models.IntegerField(null=True)

class courses_enrolled(models.Model):
    username = models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    course_name = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)

