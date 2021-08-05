from django.urls import path
from .views import MoviesView, MovieDetailView

urlpatterns = [
    path("", MoviesView.as_view()),
    path("detail/<int:pk>/", MovieDetailView.as_view())
]