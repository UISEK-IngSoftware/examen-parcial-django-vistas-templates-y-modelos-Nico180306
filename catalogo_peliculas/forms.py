from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'director', 'release_year', 'genre', 'sinopsis', 'picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
