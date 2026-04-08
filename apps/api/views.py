from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.films.models import Film
from apps.reviews.models import Review
from apps.favorites.models import Favorite
from .serializers import ReviewSerializer, FavoriteSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if film.is_blacklisted:
        return Response({'error': 'Film is blacklisted'}, status=403)
    fav = Favorite.objects.filter(user=request.user, film=film)
    if fav.exists():
        fav.delete()
        return Response({'status': 'removed'})
    Favorite.objects.create(user=request.user, film=film)
    return Response({'status': 'added'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list_create(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if film.is_blacklisted:
        return Response({'error': 'Film is blacklisted'}, status=403)
    if request.method == 'GET':
        reviews = film.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        if request.user.is_banned:
            return Response({'error': 'You are banned'}, status=403)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, film=film)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return Response(status=204)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_favorites(request):
    favorites = request.user.favorites.filter(film__is_blacklisted=False)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)