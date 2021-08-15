from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Movie, Category, Actor, Genre
from django.views.generic.base import View
from .forms import ReviewForm

class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    """kinolar royxati"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"



class MovieDetailView(GenreYear, DetailView):
    """kino xaqida batafsil ko`rish"""
    model = Movie
    slug_field = "url"



class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

class ActorView(GenreYear, DetailView):
    """aktyorlar xaqida ma`lumot"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"