from django.shortcuts import render
import requests
from django.shortcuts import redirect


def redirect_to_main(request):
    return redirect('main')


def catalog(request):
    return render(request, 'main/catalog.html')


def about(request):
    return render(request, 'main/about.html')


def top(request):
    return render(request, 'main/top.html')


