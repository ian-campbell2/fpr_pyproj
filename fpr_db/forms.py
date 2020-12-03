from django import forms
from .models import Parent, Student, Registration

class StudentResForm(forms.ModelForm):
    class Meta:
        Model = Student
        feilds = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}