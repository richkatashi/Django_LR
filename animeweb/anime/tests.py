from django.test import TestCase
from django.urls import reverse
from .models import Anime, Video
from .views import AnimeDetailView, catalog

class AnimeModelTestCase(TestCase):
    def test_anime_model_str_method(self): # Проверка метода __str__ на корректное возвращение строкового объекта
        anime = Anime.objects.create(title='Атака Титанов', anime_status='Вышел', type='TV', year=2022, anime_genres='Action', anime_studios='MAPPA', directors='Hayao Miyazaki', episodes_total=2, translations='Subtitles', description='Test anime description', poster_url='http://example.com', slug='test-anime')
        self.assertEqual(str(anime), 'Атака Титанов')

class AnimeViewTestCase(TestCase):
    def test_anime_detail_view(self): # Проверка на корректное отображение Аниме в AnimeDetailView
        anime = Anime.objects.create(title='Test Anime', anime_status='Ongoing', type='TV', year=2022, anime_genres='Action', anime_studios='Studio Ghibli', directors='Hayao Miyazaki', episodes_total=12, translations='Subtitles', description='Test anime description', poster_url='http://example.com', slug='test-anime')
        url = reverse('anime-detail', kwargs={'slug': anime.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_catalog_view(self): # Проверка catalog на корректное каталога аниме
        url = reverse('catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)