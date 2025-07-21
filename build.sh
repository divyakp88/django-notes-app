pip install -r requirements.txt
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='divya').delete(); User.objects.create_superuser('divya', 'kpdivya08@gmail.com', '123456')" | python manage.py shell
python manage.py collectstatic --noinput