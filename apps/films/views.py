from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Film, Genre

def film_list(request):
    films = Film.objects.filter(is_blacklisted=False).order_by('-release_date')
    return render(request, 'films/list.html', {'films': films})

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk, is_blacklisted=False)
    user_review = None
    if request.user.is_authenticated:
        user_review = film.reviews.filter(user=request.user).first()
    avg_rating = film.avg_rating()
    return render(request, 'films/detail.html', {
        'film': film,
        'user_review': user_review,
        'avg_rating': avg_rating,
    })

def film_search(request):
    query = request.GET.get('q', '')
    genre_id = request.GET.get('genre')
    person = request.GET.get('person', '')
    films = Film.objects.filter(is_blacklisted=False)
    if query:
        films = films.filter(title__icontains=query)
    if genre_id:
        films = films.filter(genres__id=genre_id)
    if person:
        films = films.filter(Q(actors__icontains=person) | Q(directors__icontains=person))
    genres = Genre.objects.all()
    return render(request, 'films/search.html', {'films': films, 'genres': genres, 'query': query})