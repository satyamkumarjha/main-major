from django.contrib import admin
from .models import student_details,quiz_scores,courses_enrolled


# Register your models here.

admin.site.register(student_details),
admin.site.register(quiz_scores),
admin.site.register(courses_enrolled),
