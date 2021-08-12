from django.contrib import admin
from .models import Category, Actor, Genre, RatingStar, Rating, Movie, MovieShots, Reviews
from django.utils.safestring import mark_safe

# admin.site.register(Reviews)
# admin.site.register(Actor)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60" >')
    
    get_image.short_description = "rasmlar"


class ReviewInLine(admin.StackedInline):  # ikinchi variant  admin.TabularInline
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "country", "draft",)
    list_display_links = ("id", "title",)
    list_filter = ("category", "country", "year",)
    search_fields = ("title", "category__name", "year")
    prepopulated_fields = {"url": ("title",)}
    inlines = [ReviewInLine]
    save_on_top = True  # saqlash va o`chirish tugmalarini sahifa yuqorisiga ham qo`shimcha sifatida olib chiqish uchun
    list_editable = (
    "draft",)  # admin sahifasida obyectni tashqi sahifadan turib o`zgartirish uchun (bu yerda qoralamani checkbox sifatida ishlatilyapti)
    # fields = (("actors", "directors", "genres"),)
    # fieldsets = (             #ko`rinish qismidagi malumotlarni guruhlashda foydalanamiz
    #     (None, {
    #         "fields": (("title", "tagline"),)
    #     }),
    # )


@admin.register(Reviews)
class RevievAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id",)
    readonly_fields = ("name", "email",)


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
