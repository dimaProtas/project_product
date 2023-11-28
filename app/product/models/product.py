from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Manager
from .chapter import ChapterModel


# в queryset добавлен метод not_delete, для вывода только не удалённых записей
class DeleteQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    # def get_queryset(self): # Скрывает удалённые обьекты везде и в админке
    #     qs = super().get_queryset()
    #     qs = qs.filter(deleted=False)
    #     return qs

    def get_queryset(self): # Здесь регестрируем Queryset c методом not_delete
        return DeleteQuerySet(self.model, using=self._db)


# Расширяю класс CurrentSiteManager что бы в нем был метод not_deleted()
class CustomSiteManager(CurrentSiteManager, DeletedManager):
    pass


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    provider = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    chapter = models.ManyToManyField(ChapterModel)
    site = models.ManyToManyField(Site)
    objects = DeletedManager()
    on_site = CustomSiteManager()

    def __str__(self):
        return self.name
