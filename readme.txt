python -m pip install --upgrade pip
pip install django
django-admin startproject market
cd market
python manage.py startapp market_app
python manage.py migrate
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

venv\scripts\activate

#Работа с изображениями
pip install pillow

#python manage.py makemigrations - first, python manage.py migrate - second