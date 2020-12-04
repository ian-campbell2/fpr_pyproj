from django.shortcuts import render, redirect

from .forms import StudentResForm

from .models import Camp, Student, Parent, CampRegistration

from .models import 


# Create your views here.

# request = user request of info from web page
def index(request):
    return render(request, 'fpr_db/index.html')

def camps(request):
    camps = Camp.objects.order_by('end_date')

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

def camp(request, camp_id):
    camp = Camp.objects.get(id=camp_id)

    context = {'camp':camp}

    return render(request, 'fpr_db/camp.html', context)

def students(request):
    students = Student.objects.order_by('lname')

    context = {'students':students}

    return render(request, 'fpr_db/students.html', context)

def parents(request):
    parents = Parent.objects.order_by('lname')

    context = {'parents':parents}

    return render(request, 'fpr_db/parents.html', context)

def new_camp_sign_up(request, camp_id):
    camp = Camp.objects.get(id=camp_id)
    if request.method != 'POST':

        form = CampSignUpForm()
    
    else:
        form = CampSignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('fpr_db:camp')

    context = {'form':form}
    return redirect(request, 'fpr_db/camp_sign_up.html', context)

