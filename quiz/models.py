from django.db import models
from content.models import course

# Create your models here.
# make a quiz model that has the tutorial for which this quiz is being made and also assign a quiz 
# no that helps to find which quiz is being referred to 
# then make a question model which has the tutorial and quiz number and has the question and the options for 
# that question


class quiz(models.Model):
    course_name = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)
    quiz_name = models.CharField(max_length=200)
    quiz_slug = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.quiz_name

class question(models.Model):
    course_name = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)
    quiz_name = models.ForeignKey(quiz,default=1,on_delete=models.SET_DEFAULT)
    quiz_question = models.TextField()
    option_one = models.TextField()
    option_two = models.TextField()
    option_three = models.TextField()
    option_four = models.TextField()
    picture = models.ImageField(blank = True,null=True)
    answer = models.TextField()
