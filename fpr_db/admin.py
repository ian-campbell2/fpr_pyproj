from django.contrib import admin

# Register your models here.

# add a model so you can access it from admin site
from .models import Student, Camp

admin.site.register(Student)
admin.site.register(Camp)