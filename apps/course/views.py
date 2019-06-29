from django.shortcuts import render
from django.http import HttpResponse

from apps.login.models import stu_info
from apps.course.models import course_cond
from apps.course.models import course_info
from apps.course.models import stu_course
# Create your views here.
def elective(request):
    stu = stu_info.objects.filter(username = request.session['username'])
    if len(stu)!=1:
        return HttpResponse("student information error")
    course_list = course_cond.objects.filter(department = stu[0].department).filter(grade = stu[0].grade)
    return render(request, 'elective.html',{'course_list':course_list})
    
def record(request, cno):
    #TODO:if already choose
    stu_course.objects.get_or_create(username = request.session['username'], course_no = str(cno))
    return HttpResponse('选课成功')

def giveup(request, cno):
    #TODO:if never choose
    stu_course.objects.filter(username = request.session['username'], course_no = str(cno)).delete()
    return HttpResponse('退课成功')

def list_course(request):
    course_list = stu_course.objects.filter(username = request.session['username'])
    if len(course_list)==0:
        return HttpResponse("no course")
    else:
        #暂时不知道怎么加属性，索性将课程号替换为课程名好了
        for course in course_list:
            cname = course_info.objects.filter(course_no = course.course_no)
            course.course_no = cname[0].course_name
        return render(request, 'course_list.html',{'course_list':course_list})
 
def input_grade(request, cno):
    #TODO: finish
    return HttpResponse('input_grade'+str(cno))
 
def release_homework(request, cno):
    #TODO: finish
    return HttpResponse('release_homework'+str(cno))
 