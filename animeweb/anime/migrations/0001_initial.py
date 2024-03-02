# Generated by Django 4.2.5 on 2023-10-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anime_status', models.CharField(max_length=50, verbose_name='Статус')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('year', models.IntegerField(verbose_name='Год выхода')),
                ('anime_genres', models.CharField(max_length=50, verbose_name='Жанр')),
                ('anime_studios', models.CharField(max_length=50, verbose_name='Студия')),
                ('directors', models.CharField(max_length=50, verbose_name='Режиссёр')),
                ('episodes_total', models.IntegerField(default='1', verbose_name='Количество эпизодов')),
                ('translations', models.CharField(max_length=50, verbose_name='Озвучка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster_url', models.CharField(default='Введите ссылку', max_length=250, verbose_name='Ссылка на постер')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('url', models.URLField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
    ]