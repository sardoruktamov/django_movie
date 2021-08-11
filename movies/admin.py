from django.contrib import admin
from .models import Category, Actor, Genre, RatingStar, Rating, Movie, MovieShots, Reviews

# Register your models here.

admin.site.register(Reviews)
admin.site.register(Actor)
# admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "country", "draft",)
    list_display_links = ("id", "title",)
    list_filter = ("category", "country", "year",)
    search_fields = ("title", "category__name", "year")
    prepopulated_fields = {"url": ("title",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_display_links = ("id", "name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url",)
    list_display_links = ("name", "id",)
    prepopulated_fields = {"url": ("name",)}
