from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Anime(models.Model):
    title = models.CharField('Название', max_length=50)
    anime_status = models.CharField('Статус', max_length=50)
    type = models.CharField('Тип', max_length=50)
    year = models.IntegerField('Год выхода')
    anime_genres = models.CharField('Жанр', max_length=50)
    anime_studios = models.CharField('Студия', max_length=50)
    directors = models.CharField('Режиссёр', max_length=50)
    episodes_total = models.IntegerField('Количество эпизодов', default='1') #ЭТО БУДЕТ КОЛ-ВОМ ЭПИЗОДОВ!!
    translations = models.CharField('Озвучка', max_length=50)
    description = models.TextField('Описание')
    poster_url = models.CharField('Ссылка на постер', max_length=250, default='Введите ссылку')
    slug = models.SlugField('URL', max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime-detail', kwargs={'anime_slug': self.slug})


class Meta:
    verbose_name = 'Аниме'
    verbose_name_plural = 'Аниме'


class Video(models.Model):
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50, default='')
    url = models.URLField()


    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Видео'
    verbose_name_plural = 'Видео'

