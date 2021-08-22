from django.urls import path
from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView, JsonFilterMoviesView, AddStarRating

urlpatterns = [
    path("", MoviesView.as_view()),
    path("detail/<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path("filter/", FilterMoviesView.as_view(), name="filter"),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("json-filter/", JsonFilterMoviesView.as_view(), name='json_filter'),
    path("detail/review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="actor_detail"),
]