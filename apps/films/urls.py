from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('search/', views.film_search, name='film_search'),
    path('<int:pk>/', views.film_detail, name='film_detail'),
]