from django.contrib import admin
from films.models import Film, Category


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass