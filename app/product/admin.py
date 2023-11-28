from django.contrib import admin
from . import models


@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added', 'count', 'provider', 'deleted')
    list_display_links = ['id']


@admin.register(models.ChapterModel)
class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site')
    list_display_links = ['id']