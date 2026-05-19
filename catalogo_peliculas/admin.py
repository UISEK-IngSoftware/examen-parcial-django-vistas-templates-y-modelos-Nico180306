from django.contrib import admin
from .models import Movies
# Register your models here.
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'genre')
    search_fields = ('title', 'director', 'genre')
    list_filter = ('release_year', 'genre')