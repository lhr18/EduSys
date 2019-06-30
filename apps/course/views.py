from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddHomework

from apps.login.models import stu_info
from apps.course.models import course_cond
from apps.course.models import course_info
from apps.course.models import stu_course
from apps.course.models import homework
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
    cname = course_info.objects.filter(course_no = cno)[0].course_name
    sc = stu_course.objects.filter(course_no = cno)
    for stu in sc:
        sname = stu_info.objects.filter(username = stu.username)[0].name
        stu.username = sname
    return render(request, 'input_grade.html', {'cname':cname, 'sc':sc})
 
def release_homework(request, cno):
    cname = course_info.objects.filter(course_no = cno)[0].course_name
    if request.method == 'POST':# 当提交表单时
        form = AddHomework(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            cont = form.cleaned_data['content']
            homework.objects.create(course_no = cno, content = cont)
            return HttpResponse('作业上传成功')

    else:# 当正常访问时
        form = AddHomework()
    return render(request, 'release_homework.html', {'form': form, 'cname':cname}) 
 