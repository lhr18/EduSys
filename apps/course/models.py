from django.db import models

# Create your models here.
class course_info(models.Model):
    course_no = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    course_teacher = models.CharField(max_length=30, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.course_no
       
class course_cond(models.Model):
    course_no = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    grade = models.IntegerField()
    info = models.ForeignKey(course_info, on_delete = models.CASCADE, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.course_no

class stu_course(models.Model):
    username = models.CharField(max_length=30)
    course_no = models.CharField(max_length=30)
    score = models.IntegerField(null=True, blank=True, default=None)
    
    def __str__(self):
        return self.username + ' ' + self.course_no

class homework(models.Model):
    course_no = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    
    def __str__(self):
        return self.course_no
        