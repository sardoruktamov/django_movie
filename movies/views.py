from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View


class MoviesView(View):
    """kinolar royxati"""

    def get(self, request):
        movies = Movie.objects.all()
        context = {
            "movie_list": movies,
        }
        return render(request, "movies/movie_list.html", context)


class MovieDetailView(View):
    """kino xaqida batafsil ko`rish"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        context = {
            "movie": movie,
        }
        return render(request, "movies/movie_detail.html", context)
