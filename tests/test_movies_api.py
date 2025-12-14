from http.client import responses

from Movies.fixture import json_create_movie

class TestMovies:

    def test_receiving_movies_filters(self,api_manager,):
            responce = api_manager.movies_api.receiving_movies(params = {"minPrice" :300})
            responce_json = responce.json()
            assert "id" in responce_json["movies"][0], "ID отсутствует"
            assert "name" in responce_json["movies"][0], "Название фильма отсутствует"
            movies = responce_json["movies"]
            for id_movie in movies:
                if id_movie["price"] < 300:
                    raise Exception ("Фильтр на минимальный прайс не работает")
                else:
                    pass




    def test_getting_movies(self,api_manager,):
            responce = api_manager.movies_api.receiving_movies()
            responce_json = responce.json()
            assert "id" in responce_json["movies"][0], "ID отсутствует"
            assert "name" in responce_json["movies"][0], "Название фильма отсутствует"



    def test_created_movies(self,api_manager, json_create_movie,get_movie_id):
        responce = api_manager.movies_api.get_movie(get_movie_id)
        responce_json = responce.json()
        assert "id" in responce_json, "id не найден"
        assert responce_json["name"] == json_create_movie["name"], "Имя не совпадает"
        assert responce_json["price"] == json_create_movie["price"], "price не совпадает"
        assert responce_json["description"] == json_create_movie["description"], "description не совпадает"
        assert responce_json["location"] == json_create_movie["location"], "location не свопадает"
        assert responce_json["published"] == json_create_movie["published"], "published не свопадает"
        assert responce_json["genreId"] == json_create_movie["genreId"], "genreId не совпадает"
        assert "genre" in responce_json, "genre не найден"
        assert "createdAt" in responce_json, "createdAt не найден"
        assert "rating" in responce_json, "rating не найден"


    def test_receiving_created_movies(self,api_manager,get_movie_id):
        responce = api_manager.movies_api.get_movie(get_movie_id)
        responce_json = responce.json()
        assert "id" in responce_json, "id отсутствует"
        assert "name" in responce_json, "name отсутствует"




    def test_delete_movies(self,api_manager,movie_id_without_delete):
        responce = api_manager.movies_api.delete_movies(movie_id_without_delete)
        responce_json = responce.json()
        assert "id" in responce_json, "id не найден"
        assert "name" in responce_json, "name не найден"

    def test_update_movies(self,api_manager,json_create_movie,get_movie_id):
        responce = api_manager.movies_api.update_movies(get_movie_id, json_create_movie)
        responce_json = responce.json()
        assert "id" in responce_json, "id не найден"
        assert "name" in responce_json, "name не найден"
        assert responce_json["description"] == json_create_movie["description"], "description не совпадает"
        assert responce_json["location"] == json_create_movie["location"], "location не свопадает"
        assert responce_json["published"] == json_create_movie["published"], "published не свопадает"
        assert responce_json["genreId"] == json_create_movie["genreId"], "genreId не совпадает"

