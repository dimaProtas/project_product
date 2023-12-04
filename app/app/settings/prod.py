from .base import *


SECRET_KEY = 'django-insecure-^bryk*f+1)!y+8ordi^c0m3np((0tf1^w0b0!cpydn25dl86xz'

DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1

MEDIA_ROOT = '/web/media/' #для сохранения изображений в контейнере и локально

#Запуск конфига, (можно захаркодить в manage.py что бы всегда нужный конфиг запускался, как сделано тут)
# Не забудь добавить к base dir еще один parent, так как base лежит внутри директории settings
#python manage.py runserver --settings=app.settings.prod
