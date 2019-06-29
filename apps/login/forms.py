from django import forms
 
class AddForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=30)
    password = forms.CharField(label="密码",max_length=30)