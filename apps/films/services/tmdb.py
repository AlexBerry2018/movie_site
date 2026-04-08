import requests
from django.conf import settings
from ..models import Film, Genre

class TMDBService:
    BASE_URL = "https://api.themoviedb.org/3"
    API_KEY = settings.TMDB_API_KEY

    @classmethod
    def _request(cls, path, params=None):
        params = params or {}
        params['api_key'] = cls.API_KEY
        resp = requests.get(f"{cls.BASE_URL}/{path}", params=params)
        resp.raise_for_status()
        return resp.json()

    @classmethod
    def search_movies(cls, query):
        data = cls._request("search/movie", {"query": query})
        return data.get('results', [])

    @classmethod
    def get_movie_details(cls, tmdb_id):
        data = cls._request(f"movie/{tmdb_id}", {"append_to_response": "credits,videos"})
        return data

    @classmethod
    def import_movie(cls, tmdb_id):
        data = cls.get_movie_details(tmdb_id)
        genres = []
        for g in data.get('genres', []):
            genre, _ = Genre.objects.get_or_create(tmdb_id=g['id'], defaults={'name': g['name']})
            genres.append(genre)
        actors = [cast['name'] for cast in data.get('credits', {}).get('cast', [])[:5]]
        directors = [crew['name'] for crew in data.get('credits', {}).get('crew', []) if crew['job'] == 'Director']
        trailer_key = ''
        for vid in data.get('videos', {}).get('results', []):
            if vid['site'] == 'YouTube' and vid['type'] == 'Trailer':
                trailer_key = vid['key']
                break
        film, created = Film.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                'title': data['title'],
                'overview': data.get('overview', ''),
                'release_date': data.get('release_date'),
                'poster_path': data.get('poster_path', ''),
                'backdrop_path': data.get('backdrop_path', ''),
                'trailer_key': trailer_key,
                'actors': ', '.join(actors),
                'directors': ', '.join(directors),
            }
        )
        if created or film.genres.count() == 0:
            film.genres.set(genres)
        return film