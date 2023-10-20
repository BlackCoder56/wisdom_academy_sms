from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_period = models.CharField(max_length=10)
    tuition = models.FloatField()
    
    def __str__(self):
        return f'{self.course_name}'
    
# Student table / model
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    student_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student_name}"
    
class Student_fees(models.Model):      
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE)   
    paid = models.FloatField()
   
    
    def __str__(self):
        return f"{self.student_code}"
    
class Result(models.Model):
    student_code = models.CharField(max_length=50, unique=True)
    student_name = models.CharField(max_length=30)
    m_one = models.IntegerField()
    m_two = models.IntegerField()
    m_three = models.IntegerField()
    m_four = models.IntegerField()   
    gpa = models.FloatField()

    def __str__(self):
        return f'Student: {self.student_code} {self.student_name}'