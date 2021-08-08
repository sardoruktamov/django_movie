from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Movie
from django.views.generic.base import View
from .forms import ReviewForm

class MoviesView(ListView):
    """kinolar royxati"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """kino xaqida batafsil ko`rish"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect("/")