# Generated by Django 2.2.2 on 2019-06-29 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_stu_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_cond',
            name='info',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.course_info'),
        ),
    ]