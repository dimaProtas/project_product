from django.db import models
from .chapter import ChapterModel


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    provider = models.CharField(max_length=100)
    chapter = models.ManyToManyField(ChapterModel)

    def __str__(self):
        return self.name
