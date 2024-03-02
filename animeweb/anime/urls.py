from django.urls import path
from . import views

urlpatterns = [
  path('', views.catalog, name='catalog'), # Страница каталога
  path('test', views.test),
  path('<str:slug>', views.AnimeDetailView.as_view(), name='anime-detail'),

]