from django.urls import path
from . import views

urlpatterns = [
    path('films/<int:film_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('films/<int:film_id>/reviews/', views.review_list_create, name='review_list_create'),
    path('reviews/<int:review_id>/', views.review_delete, name='review_delete'),
    path('user/favorites/', views.user_favorites, name='user_favorites'),
]