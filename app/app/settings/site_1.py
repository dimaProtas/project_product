from .prod import *


SITE_ID = 1

#Запуск конфига, (можно захаркодить в manage.py что бы всегда нужный конфиг запускался, как сделано тут)
# Не забудь добавить к base dir еще один parent, так как base лежит внутри директории settings
#python manage.py runserver --settings=app.settings.site_1