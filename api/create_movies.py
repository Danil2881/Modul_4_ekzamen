from Movies.constants import CREATE_GET_ENDPOINT
from Movies.fixture import json_create_movie
from Movies.Custom_requseter import CustomRequester
from Movies.constants import BASE_URL

# Определите ваш класс
class Create_movies(CustomRequester):
    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=BASE_URL)



    #def created_movies(self, json_create_movies):
        # responce = self.session.post(url=f"{self.base_url}{CREATE_GET_ENDPOINT}", json = json_create_movies)
        # assert responce.status_code == 201, f"Unexpected status code: {responce.status_code}"
        # self.id = responce.json().get("id")
        # print(f"Полученный id: {self.id}")
        # return responce
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
        #response = self.session.get(url=f"{self.base_url}{CREATE_GET_ENDPOINT}/{self.id}")
        responce = self.send_request(
            method="get",
            endpoint=f"{CREATE_GET_ENDPOINT}/{self.id}",
        )
        return responce

    def delete_movies(self):
        #responce = self.session.delete(url = f"{self.base_url}{CREATE_GET_ENDPOINT}/{self.id}")
        responce = self.send_request(
            method="delete",
            endpoint=f"{CREATE_GET_ENDPOINT}/{self.id}",
        )
        return responce



