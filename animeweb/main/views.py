from django.shortcuts import render
import requests

def catalog(request):
    return render(request, 'main/catalog.html')


def about(request):
    return render(request, 'main/about.html')


def top(request):
    return render(request, 'main/top.html')


