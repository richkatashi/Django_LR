from django.urls import path
from . import views

urlpatterns = [
  path('', views.redirect_to_main),
  path('main', views.catalog, name='main'), # главная страница
  path('about',views.about), # про нас
  path('top',views.top), # топ 100 аниме
  #path('test',views.test), # для теста API
]