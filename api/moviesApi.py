from Movies.constants import CREATE_GET_ENDPOINT
from Movies.fixture import json_create_movie
from Movies.Custom_requseter import CustomRequester
from Movies.constants import BASE_URL

# Определите ваш класс
class MoviesApi(CustomRequester):
    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=BASE_URL)



    def created_movies(self,data,expected_status = (200,201)):
        return self.send_request(
            method="post",
            endpoint = f"{CREATE_GET_ENDPOINT}",
            data = data,
            expected_status= expected_status
        )




    def get_movie(self,id,expected_status = (200,)):
        return self.send_request(
            method="get",
            endpoint=f"{CREATE_GET_ENDPOINT}/{id}",
            expected_status= expected_status
        )



    def receiving_movies(self,expected_status=(200,),params = None):
        return self.send_request(
            method="GET",
            endpoint= CREATE_GET_ENDPOINT,
            expected_status= expected_status,
            params = params
        )



    def delete_movies(self, id, expected_status = (200,)):
        return self.send_request(
            method="delete",
            endpoint=f"{CREATE_GET_ENDPOINT}/{id}",
            expected_status=expected_status
        )



    def update_movies(self, id, data, expected_status = (200,)):
        return self.send_request(
            method= "patch",
            endpoint = f"{CREATE_GET_ENDPOINT}/{id}",
            expected_status=expected_status,
            data = data
        )


