from django import forms

from .models import Student

class StudentResForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #fields = ['fname', 'lname', 'phone', 'bday','grade','comment']
        

'''
from .models import #CampRegistration

class CampSignUpForm(forms.ModelForm):
    class Meta:
        model = #CampRegistration
        fields = ['Fname','Lname','Paid_Or_Unpaid']
        labels = {'Fname':'Your childs first name','Lname':'Your childs last name','Paid_Or_Unpaid':'Would you like to pay in full or in installments?'}

#class StudentForm(forms.ModelForm):
'''
