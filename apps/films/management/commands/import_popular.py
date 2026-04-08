from django.core.management.base import BaseCommand
from apps.films.services.tmdb import TMDBService

class Command(BaseCommand):
    help = 'Imports popular movies from TMDB'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=20, help='Number of movies to import')

    def handle(self, *args, **options):
        count = options['count']
        data = TMDBService._request('movie/popular', {'page': 1})
        for movie in data['results'][:count]:
            TMDBService.import_movie(movie['id'])
            self.stdout.write(f"Imported: {movie['title']}")
        self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} movies"))