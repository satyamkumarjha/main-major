from django.db import models

# Create your models here.

class teacherData(models.Model):
    teacher_name = models.CharField(max_length=200)
    Education = models.CharField(max_length=400)
    facebook_id = models.SlugField(max_length=400)
    instagram_id = models.SlugField(max_length=400)
    email_id = models.SlugField(max_length=400)
    tag_line = models.CharField(max_length=400)
    teacher_image = models.ImageField(blank=True)
    def __str__(self):
        return self.teacher_name
