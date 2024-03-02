from django.urls import path
from . import views

urlpatterns = [
  path('', views.catalog), # главная страница
  path('about',views.about), # про нас
  path('top',views.top), # топ 100 аниме
  #path('test',views.test), # для теста API
]