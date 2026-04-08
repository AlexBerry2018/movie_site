from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # добавьте этот импорт

urlpatterns = [
    path('', lambda request: redirect('film_list', permanent=False)),  # перенаправление на films/
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.users.urls')),
    path('films/', include('apps.films.urls')),
    path('api/', include('apps.api.urls')),
]