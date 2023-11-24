from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('chapters/', views.ChapterListView.as_view(), name='chapter-list'),
    path('chapter_goods/<int:pk>/', views.ChapterGoodsListView.as_view(), name='chapter-goods')
]
