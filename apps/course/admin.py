from django.contrib import admin
from .models import course_info
from .models import course_cond
from .models import stu_course
from .models import homework

# Register your models here.
admin.site.register(course_info)
admin.site.register(course_cond)
admin.site.register(stu_course)
admin.site.register(homework)