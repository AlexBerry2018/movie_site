from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.action(description='Заблокировать выбранных пользователей')
def block_users(modeladmin, request, queryset):
    queryset.update(is_banned=True)

@admin.action(description='Разблокировать')
def unblock_users(modeladmin, request, queryset):
    queryset.update(is_banned=False)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_banned', 'is_staff')
    list_filter = ('is_banned', 'is_staff')
    actions = [block_users, unblock_users]
    fieldsets = UserAdmin.fieldsets + (('Доп. инфо', {'fields': ('bio', 'avatar_url', 'is_banned')}),)

admin.site.register(User, CustomUserAdmin)