from django.contrib import admin
from .models import Anime, Video
import requests
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')

    def save_model(self, request, obj, form, change):
        print('save_model called')
        # Добавляем "https:" к значению поля url, если оно не начинается с "http" или "https"
        if obj.url and not obj.url.startswith(('http:', 'https:')):
            obj.url = f'https:{obj.url}'
        obj.save()


admin.site.register(Video, VideoAdmin)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0  # не отображать пустые строчки


class AnimeAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    prepopulated_fields = {"slug": ("title",), }


admin.site.register(Anime, AnimeAdmin)