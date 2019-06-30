"""EduSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.login import views as login_views
from apps.course import views as course_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addusers/', login_views.addusers),#用于测试时初始化数据库
    path('login/', login_views.login),
    path('elective/', course_views.elective, name='ele_course'),
    path('list_course/', course_views.list_course, name='list_course'),
    path('record/<int:cno>/', course_views.record, name='record'),
    path('giveup/<int:cno>/', course_views.giveup, name='giveup'),
    path('input_grade/<int:cno>/', course_views.input_grade, name='input_grade'),
    path('release_homework/<int:cno>/', course_views.release_homework, name='release_homework'),
    path('course_homepage/<str:cname>/', course_views.course_homepage, name='course_homepage'),#注意，参数是字符串型的课程名字
]
