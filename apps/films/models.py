from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    overview = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    poster_path = models.CharField(max_length=300, blank=True)
    backdrop_path = models.CharField(max_length=300, blank=True)
    trailer_key = models.CharField(max_length=50, blank=True)
    genres = models.ManyToManyField(Genre, related_name='films')
    actors = models.TextField(blank=True)
    directors = models.TextField(blank=True)
    is_blacklisted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def poster_url(self):
        return f"https://image.tmdb.org/t/p/w500{self.poster_path}" if self.poster_path else ""

    def avg_rating(self):
        from apps.reviews.models import Review
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0