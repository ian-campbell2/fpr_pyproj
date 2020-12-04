# comments in power point to help understand this page

from django.urls import path
from . import views

app_name = 'fpr_db'

urlpatterns = [
    path('',views.index, name='index'),
    path('camps/',views.camps, name='camps'),
    path('new_student/', views.new_student, name='new_student'),
    path('camp', views.camp, name='camp'),
    path('students',views.students, name='students'),
    path('parents',views.parents, name='parents'),
    #path('camp_sign_up/<int:camp_id>/', views.camp_sign_up, name='camp_sign_up'),
]