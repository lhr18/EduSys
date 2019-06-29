from django.db import models

# Create your models here.
class user_pwd(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.IntegerField()
    
    def __str__(self):
        return self.username
