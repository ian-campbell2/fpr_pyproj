from django import forms
from .models import Student

class StudentResForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #fields = ['fname', 'lname', 'phone', 'bday','grade','comment']
        