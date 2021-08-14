from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Movie, Category
from django.views.generic.base import View
from .forms import ReviewForm

class MoviesView(ListView):
    """kinolar royxati"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movie_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context

class MovieDetailView(DetailView):
    """kino xaqida batafsil ko`rish"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context

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