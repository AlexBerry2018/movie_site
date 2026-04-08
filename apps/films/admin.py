from django.contrib import admin
from .models import Film, Genre

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'is_blacklisted')
    list_editable = ('is_blacklisted',)
    search_fields = ('title',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'tmdb_id')