from django import forms

from .models import Parent, Student, Registration

class StudentResForm(forms.ModelForm):
    class Meta:
        Model = Student
        feilds = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

'''
from .models import #CampRegistration

class CampSignUpForm(forms.ModelForm):
    class Meta:
        model = #CampRegistration
        fields = ['Fname','Lname','Paid_Or_Unpaid']
        labels = {'Fname':'Your childs first name','Lname':'Your childs last name','Paid_Or_Unpaid':'Would you like to pay in full or in installments?'}

#class StudentForm(forms.ModelForm):
'''

