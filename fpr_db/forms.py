from django import forms

from .models import Student, CampRegistration, Parent

class StudentResForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        #fields = ['fname', 'lname', 'phone', 'bday','grade','comment']
        



class CampSignUpForm(forms.ModelForm):
    class Meta:
        model = CampRegistration
        fields = ['student','payment_received']
        labels = {'student':"Enter your child's ID",'payment_received':'Would you like to pay now? (Y or N)'}

