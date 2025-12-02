from Movies.api.conftest import test_user
from Movies.fixture import json_create_movie

class TestMovies:

    def test_receiving_movies(self,api_manager):
        responce = api_manager.receiving_api.receiving_movies()
        responce_json = responce.json()
        assert responce.status_code == 200, "Статус код не верный"
        assert "id" in responce_json["movies"][0], "ID отсутствует"
        assert "name" in responce_json["movies"][0], "Название фильма отсутствует"


    def test_created_movies(self,api_manager,json_create_movie):
        responce = api_manager.create_movies.created_movies(json_create_movie)
        responce_json = responce.json()
        assert responce.status_code == 201, f"Статус код не верный"
        assert "id" in responce_json, "id не найден"
        assert responce_json["name"] == json_create_movie.get("name"), "Имя не совпадает"
        assert responce_json["price"] == json_create_movie.get("price"), "price не совпадает"
        print(responce_json)

    def test_receiving_created_movies(self,api_manager):
        responce = api_manager.create_movies.receiving_created_movies()
        responce_json = responce.json()
        assert responce.status_code == 200, "не верный статус код при получении"
        assert "id" in responce_json, "id отсутствует"
        assert "name" in responce_json, "name отсутствует"



    def test_delete_movies(self,api_manager):
        responce = api_manager.create_movies.delete_movies()
        responce_json = responce.json()
        assert responce.status_code == 200, "Не верный статус код"
        assert "id" in responce_json, "id не найден"
        assert "name" in responce_json, "name не найден"