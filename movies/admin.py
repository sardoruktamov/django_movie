# from django import forms
from django import forms
from django.contrib import admin
from .models import Category, Actor, Genre, RatingStar, Rating, Movie, MovieShots, Reviews
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Kino tavsifi", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

admin.site.register(RatingStar)
admin.site.register(Rating)

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60" >')

    get_image.short_description = "rasm"

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60" >')
    
    get_image.short_description = "rasm"


class ReviewInLine(admin.StackedInline):  # ikinchi variant  admin.TabularInline
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email",)

class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="70" >')

    get_image.short_description = "rasm"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "country", "draft",)
    list_display_links = ("id", "title",)
    list_filter = ("category", "country", "year",)
    search_fields = ("title", "category__name", "year")
    prepopulated_fields = {"url": ("title",)}
    inlines = [MovieShotsInLine, ReviewInLine]
    save_on_top = True  # saqlash va o`chirish tugmalarini sahifa yuqorisiga ham qo`shimcha sifatida olib chiqish uchun
    save_as = True
    list_editable = ("draft",)  # admin sahifasida obyectni tashqi sahifadan turib
                                # o`zgartirish uchun (bu yerda qoralamani checkbox sifatida ishlatilyapti)
    form = MovieAdminForm
    actions = ["publish", "unpublish"]
    readonly_fields = ("get_image",)
    # fields = (("actors", "directors", "genres"),)
    # fieldsets = (             #ko`rinish qismidagi malumotlarni guruhlashda foydalanamiz
    #     ("Actors", {
    #         "fields": (("deskription", "poster"),)
    #     }),
    # )

    def unpublish(self, request, queryset):
        """Nashrdan chiqarish"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 ta yozuv yangilandi"
        else:
            message_bit = f"{row_update} yozuvlar yangilandi"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Nashr qilish"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 ta yozuv yangilandi"
        else:
            message_bit = f"{row_update} yozuvlar yangilandi"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Nashr qilish"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Nashrdan chiqarish"
    unpublish.allowed_permissions = ('change',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="60" height="70" >')

    get_image.short_description = "asosiy rasm"

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


admin.site.site_title = "Django movies"
admin.site.site_header = "Boshqaruv paneli"