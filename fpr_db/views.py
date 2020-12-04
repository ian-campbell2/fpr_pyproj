from django.shortcuts import render, redirect
from .models import Camp, Student
from .forms import StudentResForm

# Create your views here.

# request = user request of info from web page
def index(request):
    return render(request, 'fpr_db/index.html')

def camps(request):
    camps = Camp.objects.order_by(start_date)

    context = {'camps':camps}

    return render(request, 'fpr_db/camps.html', context)

def new_student(request):
    if request.method != 'POST':
        form = StudentResForm()
    else:
        form = StudentResForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('fpr_db:base')

    context = {'form':form}

    return render(request, 'fpr_db/new_student.html', context)