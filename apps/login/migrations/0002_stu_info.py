# Generated by Django 2.2.2 on 2019-06-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stu_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=30)),
                ('grade', models.IntegerField()),
            ],
        ),
    ]
