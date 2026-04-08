# Развертывание Movie Catalog

## Требования
- Python 3.10+
- PostgreSQL
- API-ключ [TMDB](https://www.themoviedb.org/signup)

## Установка

1. Клонировать репозиторий

   ```bash
   git clone https://github.com/AlexBerry2018/movie-catalog.git
   cd movie-catalog
   ```
2. Создать виртуальное окружение

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\\Scripts\\activate         # Windows
   ```
3. Установить зависимости
   ```bash
   pip install -r requirements.txt
   ```
4. Создать файл .env в корне проекта:

   ```env
   SECRET_KEY=ваш_секретный_ключ
   TMDB_API_KEY=ваш_ключ_tmdb
   DB_NAME=movie_db
   DB_USER=postgres
   DB_PASSWORD=ваш_пароль
   DB_HOST=localhost
   DB_PORT=5432
   DEBUG=True
   ```
5. Генерация SECRET_KEY:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
6. Создать базу данных PostgreSQL
   ```sql
   CREATE DATABASE movie_db;
   ```
7. Выполнить миграции

   ```bash
   python manage.py migrate
   ```
8. Создать суперпользователя

   ```bash
   python manage.py createsuperuser
   ```
9. Импортировать фильмы из TMDB

   ```bash
   python manage.py import_popular --count 30
   ```
10. Запустить сервер

   ```bash
   python manage.py runserver
   ```
11. Открыть в браузере – http://127.0.0.1:8000
