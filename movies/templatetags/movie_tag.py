from django import template
from movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    """barcha categoriyalarni chiqarish"""
    return Category.objects.all()

# def get_last_movies():
#     movies = Movie.objects.order_by("id")[:5]
#     return {}