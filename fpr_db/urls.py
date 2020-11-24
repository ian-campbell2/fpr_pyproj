# comments in power point to help understand this page

from django.urls import path
from . import views

app_name = 'fpr_db'

urlpatterns = [
    path('',views.index, name='index'),
    path('camps',views.camps, name='camps'),
]