from Movies.constants import CREATE_GET_ENDPOINT
from Movies.fixture import json_create_movie
from Movies.Custom_requseter import CustomRequester
from Movies.constants import BASE_URL

# Определите ваш класс
class Create_movies(CustomRequester):
    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=BASE_URL)



    def created_movies(self,json_create_movies):
        responce = self.send_request(
            method="post",
            endpoint = f"{CREATE_GET_ENDPOINT}",
            data = json_create_movies,
        )
        self.id = responce.json().get("id")
        print(self.id)
        return responce


    def receiving_created_movies(self):
        responce = self.send_request(
            method="get",
            endpoint=f"{CREATE_GET_ENDPOINT}/{self.id}",
        )
        return responce

    def delete_movies(self):
        responce = self.send_request(
            method="delete",
            endpoint=f"{CREATE_GET_ENDPOINT}/{self.id}",
        )
        return responce



