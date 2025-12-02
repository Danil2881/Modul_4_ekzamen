from Movies.api.conftest import test_user
from Movies.fixture import json_create_movie

class TestMovies:
    def test_receiving_posters(self,api_manager,test_user):
        responce = api_manager.receiving_api.receiving_posters(test_user)
        responce_json = responce.json()
        print(responce_json)

    def test_receiving_movies(self,api_manager):
        responce = api_manager.receiving_api.receiving_movies()
        responce_json = responce.json()

    def test_created_movies(self,api_manager,json_create_movie):
        responce = api_manager.create_movies.created_movies(json_create_movie)
        responce_json = responce.json()

    def test_receiving_created_movies(self,api_manager,json_create_movie):
        responce = api_manager.create_movies.receiving_created_movies()
