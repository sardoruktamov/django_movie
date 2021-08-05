from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
from django.views.generic.base import View


class MoviesView(ListView):
    """kinolar royxati"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """kino xaqida batafsil ko`rish"""
    model = Movie
    slug_field = "url"
