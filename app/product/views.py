from django.shortcuts import render
from django.db.models import Prefetch
from django.views.generic import ListView, DetailView
from . import models


class ProductListView(ListView):
    # queryset = models.ProductModel.objects.all()
    # оптимизация запроса с помощью prefetch_related (потомучто связаное поле ManyToMany)
    queryset = models.ProductModel.objects.prefetch_related('chapter').all()
    template_name = 'goods_list.html'
    context_object_name = 'objects_list'


class ChapterListView(ListView):
    queryset = models.ChapterModel.objects.prefetch_related(
        Prefetch('productmodel_set', queryset=models.ProductModel.objects.only('name', 'date_added', 'count', 'provider'))
    ).all()
    template_name = 'chapter_list.html'
    context_object_name = 'chapters_list'




class ChapterGoodsListView(DetailView):
    template_name = 'goods_list.html'
    context_object_name = 'objects_list'
    model = models.ChapterModel

    # Без оптимизации запросов
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['objects_list'] = self.get_object().productmodel_set.all()
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Оптимизация запроса с использованием prefetch_related
        chapter_with_products = models.ChapterModel.objects.prefetch_related(
            Prefetch('productmodel_set',
                     queryset=models.ProductModel.objects.only('name', 'date_added', 'count', 'provider'))
        ).get(pk=self.kwargs['pk'])

        context['objects_list'] = chapter_with_products.productmodel_set.all()
        return context

