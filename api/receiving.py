from Movies.constants import CREATE_GET_ENDPOINT
from Movies.Custom_requseter import CustomRequester

class ReceivingApi(CustomRequester):
    def __init__(self,session):
        super().__init__(session=session,base_url="https://api.dev-cinescope.coconutqa.ru")


    def receiving_posters(self,data_user,expected_status=200):
        return self.send_request(
           method = "GET",
           endpoint = CREATE_GET_ENDPOINT,
           expected_status=expected_status
        )

    def receiving_movies(self,expected_status=200):
        return self.send_request(
            method="GET",
            endpoint= CREATE_GET_ENDPOINT,
            expected_status=expected_status
        )