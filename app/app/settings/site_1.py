from .prod import *
import os

print(os.environ.get('DJANGO_SETTINGS_MODULE'))

SITE_ID = 1

CSRF_USE_SESSIONS = True
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://web'] #Без этого не работает авторизация в админке


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_database',
        'USER': 'dima',
        'PASSWORD': 'dima',
        'HOST': 'db',
        'PORT': '5432',
    }
}


#Запуск конфига, (можно захаркодить в manage.py что бы всегда нужный конфиг запускался, как сделано тут)
# Не забудь добавить к base dir еще один parent, так как base лежит внутри директории settings
#python manage.py runserver --settings=app.settings.site_1
