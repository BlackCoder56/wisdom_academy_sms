from django.contrib import admin
from . models import Course, Result, Student, Student_fees


# Register your models here.
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Student)
admin.site.register(Student_fees)