from django.shortcuts import render, get_object_or_404
from .models import Anime, Video
from django.views.generic import DetailView
import requests
# Create your views here.

API_TOKEN = '95c3495f0096478e2930702f5b704b0f'

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/details_view.html'
    context_object_name = 'anime'

    def get_object(self, queryset=None):
        anime_slug = self.kwargs.get('slug')
        return get_object_or_404(Anime, slug=anime_slug)

def catalog (request):
    anime = Anime.objects.all()
    return render(request, 'main/catalog.html', {'anime': anime})


def test(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            url = 'https://kodikapi.com/search'
            params = {
                'token': API_TOKEN,
                'title': search_query,
                'types': 'anime-serial,anime',
                'with_material_data': 'true',
                'with_episodes': 'true',
                'full_match': 'true',
            }
            response = requests.get(url, params=params).json()
            return render(request, 'main/test.html', {'response': response})
    else:
        return render(request, 'main/test.html')
    return render(request, 'main/test.html')