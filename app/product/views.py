from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms


class BaseView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class()
        context.update({
            'site': get_current_site(request=self.request)
        })
        return context


class ProductListView(BaseView):
    # queryset = models.ProductModel.objects.all()
    # оптимизация запроса с помощью prefetch_related (потомучто связаное поле ManyToMany)
    queryset = models.ProductModel.on_site.prefetch_related('chapter').not_deleted().all()
    template_name = 'goods_list.html'
    context_object_name = 'objects_list'
    form_class = forms.FormProduct

    def post(self, request, *args, **kwargs):
        # Логика обработки POST-запроса
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return self.get(request, *args, **kwargs)


class ChapterListView(BaseView):
    queryset = models.ChapterModel.on_site.prefetch_related(
        Prefetch('productmodel_set', queryset=models.ProductModel.objects.only('name', 'date_added', 'count', 'provider'))
    ).all()
    template_name = 'chapter_list.html'
    context_object_name = 'chapters_list'
    form_class = forms.ChapterForm

    def post(self, request, *args, **kwargs):
        # Логика обработки POST-запроса
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/chapters/')
        return self.get(request, *args, **kwargs)


class ChapterGoodsListView(BaseView):
    template_name = 'goods_list.html'
    context_object_name = 'objects_list'
    model = models.ChapterModel
    form_class = forms.ChapterForm

    # Без оптимизации запросов
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['objects_list'] = self.get_object().productmodel_set.all()
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Оптимизация запроса с использованием prefetch_related
        chapter_with_products = models.ChapterModel.on_site.prefetch_related(
            Prefetch('productmodel_set',
                     queryset=models.ProductModel.objects.only('name', 'date_added', 'count', 'provider'))
        ).get(pk=self.kwargs['pk'])

        context['objects_list'] = chapter_with_products.productmodel_set.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/chapters/')
        return self.get(request, *args, **kwargs)


def delete_chapter(request, chapter_id):
    chapter = models.ChapterModel.objects.get(id=chapter_id)
    if request.method == 'POST':
        chapter.delete()
    return redirect('chapter-list')
