from django.urls import path
from .views import MoviesView, MovieDetailView, AddReview

urlpatterns = [
    path("", MoviesView.as_view()),
    path("detail/<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("detail/review/<int:pk>/", AddReview.as_view(), name="add_review"),
]