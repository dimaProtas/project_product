from django.contrib.sites.models import Site
from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Manager


class ChapterModel(models.Model):
    name = models.CharField(max_length=100, default=None)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()  # Менеджер выводит всю информацию если использовать в view
    on_site = CurrentSiteManager('site') # Выводит только для выбранного сайта в settings

    def __str__(self):
        return self.name

