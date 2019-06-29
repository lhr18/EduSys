# 综合教务系统
## 介绍
我们尝试使用Django编写一个综合教务系统的demo
在windows 10 下开发  
~~用到数据库mysql，如果想要正常运行，建议在数据库中添加对应的表，同时修改settings.py中与数据库相关的设置。~~（暂时不使用mysql，而是使用django自带的数据库）  
对了，有一个事情我还没想清楚，就是数据库查询的时候出现中文，会不会有什么问题？  

## 目录
.  
|-EduSys  
|   |-settings.py  
|   |-urls.py  
|   |-wsgi.py  
|-README.md  
|-apps  
|   |-course  
|   |   |-admin.py  
|   |   |-apps.py  
|   |   |-models.py  
|   |   |-templates  
|   |   |   |-course_list.html  
|   |   |   |-elective.html  
|   |   |-tests.py  
|   |   |-views.py  
|   |-login  
|       |-admin.py  
|       |-apps.py  
|       |-forms.py  
|       |-models.py  
|       |-templates  
|       |   |-login.html  
|       |   |-stu_page.html  
|       |   |-tch_page.html  
|       |-tests.py  
|       |-views.py  
|-db.sqlite3  
|-doc  
|   |-flowchart.png  
|-manage.py  
|-media  
|-static  
|-templates  


## 数据库设计
1. 用户登录信息管理（用户名、密码、身份）
2. 学生个人信息（用户名、姓名、院系、年级）
3. 教师个人信息（用户名、教师姓名）
4. 课程信息（课程号、课程名、教师（用户名）、上课时间）（可能有多个时间）（暂时不考虑上课时间吧）
5. 选课条件（课程号、院系、年级）
6. 学生选课记录（用户名、课程号、成绩）
7. 课程作业（课程号、作业内容）（要保存为文件索引吗？）

## 抽空再加点东西
- 退出登录（切换用户）
- 学生进入课程主页，查看作业记录

## 更新日志
### [0.0.0] 2019-6-11
#### Added
- 什么也没写，今天有点时间，就先把项目建起来。
### [0.0.1] 2019-6-29
#### Added
- 把登录模块做完了，验证并保存登录信息，跳转到用户主页。  
- 将数据库改为django自带的sqlite3  
### [0.0.2] 2019-6-29
#### Added
- 学生模块完成，包括选课退课、查看课表和成绩  
- 教师模块开了个头，具体功能还没有实现