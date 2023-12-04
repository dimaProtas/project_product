from django import forms
from .models import ChapterModel, ProductModel


class FormProduct(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ChapterForm(forms.ModelForm):
    class Meta:
        model = ChapterModel
        fields = '__all__'
