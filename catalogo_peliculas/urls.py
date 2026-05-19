from django.urls import path
from . import views

app_name = 'catalogo_peliculas'

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.movie_list, name='movie_list'),
    path('peliculas/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
