from django.shortcuts import render
from .models import Camp

# Create your views here.

# request = user request of info from web page
def index(request):
    return render(request, 'fpr_db/index.html')

def camps(request):
    camps = Camp.objects.order_by(start_date)

    context = {'camps':camps}

    return render(request, 'fpr_db/camps.html', context)