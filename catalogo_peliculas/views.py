from django.shortcuts import render, get_object_or_404
from .models import Movies

# Create your views here.

def index(request):
    movies = Movies.objects.all()
    return render(request, 'catalogo_peliculas/movie_list.html', {'movies': movies})


def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'catalogo_peliculas/movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    return render(request, 'catalogo_peliculas/movie_detail.html', {'movie': movie})

