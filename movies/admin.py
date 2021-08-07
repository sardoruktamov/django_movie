from django.contrib import admin
from .models import Category, Actor, Genre, RatingStar, Rating, Movie, MovieShots

# Register your models here.

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Movie, MovieAdmin)
