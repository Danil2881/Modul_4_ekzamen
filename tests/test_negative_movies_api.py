from Movies.fixture import json_create_movie
import requests
from Movies.api.moviesApi import MoviesApi
from Movies.constants import BASE_URL

class TestNegativeMovie:

    def test_negative_created_movies(self,json_create_movie):
        """Отсутствие Авторизации"""
        session = requests.Session()
        api = MoviesApi(session,BASE_URL)
        responce = api.created_movies (json_create_movie, expected_status= (401,))
        # assert responce.status_code == 401, "Не верный статус код"

    def test_negative_created_data(self,api_manager):
        responce = api_manager.movies_api.created_movies(data = {"name" : "movies", "price" : 300}, expected_status=(400,))
        # assert responce.status_code == 400, "Статус код не верный"

    def test_negative_get_non_existent_movie(self,getting_remote_id,api_manager):
        responce = api_manager.movies_api.get_movie(getting_remote_id, expected_status=(404,))
        # assert responce.status_code == 404, "Статус код не верный"

    def test_negative_delete_non_existent_movie(self,getting_remote_id,api_manager):
        responce = api_manager.movies_api.delete_movies(getting_remote_id, expected_status=(404,))
        # assert responce.status_code == 404, "Статус код не верный"

    def test_negative_created_an_existing_movie(self,movie_id_without_delete,json_create_movie,api_manager):
        get_movie = api_manager.movies_api.get_movie(movie_id_without_delete)
        json_movie = get_movie.json()
        responce = api_manager.movies_api.created_movies(json_movie, expected_status= (409,))
        # assert responce.status_code == 409, "Статус код не верный"
