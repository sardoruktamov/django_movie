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


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}
admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
admin.site.register(Genre, GenreAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
admin.site.register(Category, CategoryAdmin)