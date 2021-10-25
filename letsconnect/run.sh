python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('squareboat', 'support@squareboat.com', 'squareboat')" | python manage.py shell
django-admin loaddata  db.json -i  
# python manage.py runserver 0.0.0.0:$PORT
echo "RUN SCRIPT FINISHED"
