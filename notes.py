'''
migrations
any time want to change db, need make a migration file
python3 manage.py makemigrations fpr_db
can see each migration file in the migrations folder
python3 manage.py migrate


to make model accessable from admin site:
from .models import blah, model_name
admin.site.register(model_name)


views render information onto the template
1 define address of page you want to view in urls in the app
2 write the view
3 write the html template
when urls searched, they  search for the corresponding view
 

python3 manage.py createsuperuser
admin login: adminfpr, adminpw
'''