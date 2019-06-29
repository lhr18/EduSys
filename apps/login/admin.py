from django.contrib import admin
from .models import user_pwd
from .models import stu_info

# Register your models here.
admin.site.register(user_pwd)
admin.site.register(stu_info)