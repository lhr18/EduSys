from django.shortcuts import render
from django.http import HttpResponse

from apps.login.models import stu_info
from apps.course.models import course_cond
# Create your views here.
def elective(request):
    stu = stu_info.objects.filter(username = request.session['username'])
    if len(stu)!=1:
        return HttpResponse("student information error")
    course_list = course_cond.objects.filter(department = stu[0].department).filter(grade = stu[0].grade)
    return render(request, 'elective.html',{'course_list':course_list})
    
def record(request, cno):
    
    return HttpResponse(str(cno))
    