from django import forms

class AddHomework(forms.Form):
    content = forms.CharField(label="作业描述",max_length=50)