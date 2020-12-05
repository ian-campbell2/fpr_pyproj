from django.shortcuts import render, redirect

from .forms import StudentResForm, CampSignUpForm

from .models import Camp, Student, Parent, CampRegistration

from django.contrib.auth.decorators import login_required

from django.http import Http404

#from .models import 


# Create your views here.

# request = user request of info from web page
def index(request):
    return render(request, 'fpr_db/index.html')

@login_required
def camps(request):
    camps = Camp.objects.order_by('end_date')

    context = {'camps':camps}

    return render(request, 'fpr_db/camps.html', context)

@login_required
def new_student(request):
    if request.method != 'POST':
        form = StudentResForm()
    else:
        form = StudentResForm(data=request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.owner = request.user
            new_student.save()
            return redirect('fpr_db:students')

    context = {'form':form}

    return render(request, 'fpr_db/new_student.html', context)

@login_required
def camp(request, camp_id):
    camp = Camp.objects.get(id=camp_id)

    context = {'camp':camp}

    return render(request, 'fpr_db/camp.html', context)

@login_required
def students(request):
    students = Student.objects.filter(owner=request.user).order_by('lname')

    context = {'students':students}

    return render(request, 'fpr_db/students.html', context)

@login_required
def parents(request):
    parents = Parent.objects.order_by('lname')

    context = {'parents':parents}

    return render(request, 'fpr_db/parents.html', context)

@login_required
def camp_sign_up(request, camp_id):
    camp = Camp.objects.get(id=camp_id)
    if request.method != 'POST':

        form = CampSignUpForm()
    
    else:
        form = CampSignUpForm(data=request.POST)

        if form.is_valid():
            camp_sign_up = form.save(commit=False)
            camp_sign_up.camp = camp
            camp_sign_up.save()
            form.save()
            return redirect('fpr_db:camp', camp_id=camp_id)

    context = {'form':form, 'camp':camp}
    return redirect(request, 'fpr_db/camp_sign_up.html', context)

