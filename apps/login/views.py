from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

from apps.login.models import user_pwd
 
def addusers(request):
    user_pwd.objects.create(username="lhr", password="111", role=1)
    user_pwd.objects.create(username="yzq", password="222", role=1)
    user_pwd.objects.create(username="ljr", password="333", role=1)
    user_pwd.objects.create(username="wyf", password="444", role=1)
    return HttpResponse("Initialization")

def login(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        
        if form.is_valid():# 如果提交的数据合法
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            pwd_check = user_pwd.objects.filter(username = uname)
            if len(pwd_check)>1:
                return HttpResponse('please check database')
            elif len(pwd_check)==0:
                return HttpResponse('username error')
            elif pwd_check[0].password == pwd and pwd_check[0].role == 1:
                request.session['username'] = uname
                #request.session['role'] = 1
                return render(request,'stu_page.html',{'username':uname})
            elif pwd_check[0].password == pwd and pwd_check[0].role == 2:
                request.session['username'] = uname
                #request.session['role'] = 2
                return render(request,'tch_page.html',{'username':uname})
            else:
                return HttpResponse('wrong password')

    else:# 当正常访问时
        form = AddForm()
    return render(request, 'login.html', {'form': form}) 
 