from django.contrib import admin
from .models import Review

@admin.action(description='Удалить выбранные отзывы')
def delete_reviews(modeladmin, request, queryset):
    queryset.delete()

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('film', 'user', 'rating', 'created_at')
    actions = [delete_reviews]