import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","fpr.settings")

import django
django.setup()

from fpr_db.models import Student

students = Student.objects.all()

for stud in students:
    print("Student ID:", student.id, "Student:", student)


s = Student.objects.get(id=2)
print(s.text)
print(s.lname)


## 25:00 II
camps = t.ent