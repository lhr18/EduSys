from django import forms

class AddHomework(forms.Form):
    content = forms.CharField(label="作业描述",max_length=50)

class AddScore(forms.Form):
    name = forms.CharField(label="姓名",max_length=10)
    score = forms.IntegerField(label="录入分数")
