from django.db import models
from datetime import date


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Kategoriya", max_length=150)
    description = models.TextField("Izox")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "kategoriyalar"


class Actor(models.Model):
    name = models.CharField("Nomi", max_length=100)
    age = models.PositiveSmallIntegerField("Yosh", default=0)
    description = models.TextField("Izox")
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Aktyor va rejissior"
        verbose_name_plural = "Aktyor va rejissiorlar"


class Genre(models.Model):
    name = models.CharField("Nomi", max_length=150)
    description = models.TextField("Izox")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Movie(models.Model):
    title = models.CharField("sarlavha", max_length=100)
    tagline = models.CharField("spogan", max_length=100, default='')
    description = models.TextField("Izox")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("ishlab chiqilgan yil", default=2020)
    country = models.CharField("davlat", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="rejissior", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Aktyor", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Janr")
    world_premiere = models.DateField("Jaxon primyerasi", default=date.today())
    budget = models.PositiveIntegerField("Byudjet", default=0, help_text="summa do'llorda ko'rsatilgan")
    fees_in_usa = models.PositiveIntegerField("AQSH tulovlari", default=0, help_text="summa do'llorda ko'rsatilgan")
    fees_in_world = models.PositiveIntegerField("AQSH tulovlari", default=0, help_text="summa do'llorda ko'rsatilgan")
    category = models.ForeignKey(Category, verbose_name="Kategoriya", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Qoralama", default=False)

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "filmlar"


class MovieShots(models.Model):
    title = models.CharField("sarlavha", max_length=100)
    description = models.TextField("Izox")
    image = models.ImageField("rasm", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Kino", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "filmdan kadr"
        verbose_name_plural = "filmdan kadrlar"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Yulduzcha", default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "reyting yulduzcha"
        verbose_name_plural = "reyting yulduzchalari"


class Rating(models.Model):
    ip = models.CharField("IP adres", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="yulduzcha")
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="kino")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "reyting"
        verbose_name_plural = "reytinglar"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Ism", max_length=100)
    text = models.TextField("Xabar", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Uziniki', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="kino")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "kurib chiqish"
        verbose_name_plural = "kurib chiqishlar"
