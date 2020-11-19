'''
migrations
any time want to change db, need make a migration file
python3 manage.py makemigrations app_name
can see each migration file in the migrations folder
python3 manage.py migrate


to make model accessable from admin site:
from .models import blah, model_name
admin.site.register(model_name)

'''