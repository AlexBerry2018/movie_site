from rest_framework import serializers
from apps.reviews.models import Review
from apps.favorites.models import Favorite
from apps.films.models import Film

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = ['id', 'rating', 'text', 'created_at', 'username']
        read_only_fields = ['user', 'film']

class FilmMiniSerializer(serializers.ModelSerializer):
    poster_url = serializers.ReadOnlyField()
    class Meta:
        model = Film
        fields = ['id', 'title', 'poster_url']

class FavoriteSerializer(serializers.ModelSerializer):
    film = FilmMiniSerializer()
    class Meta:
        model = Favorite
        fields = ['id', 'film', 'added_at']