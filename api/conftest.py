from Movies.Custom_requseter import CustomRequester
import pytest
import requests
from Movies.utils.datagenerator import DataGenerator
from Movies.api.api_manager import ApiManager
from Movies.constants import BASE_URL

@pytest.fixture()
def test_user():
        random_email =DataGenerator.generate_email()
        random_name = DataGenerator.generate_name()
        random_password = DataGenerator.generate_random_password()

        return{
            "email" : random_email,
            "fullname" : random_name,
            "password": random_password,
            "passwordRepeat": random_password,
            "roles":["USER"]
        }
#@pytest.fixture()
#def registered_user(requester,test_user):
        #responce = CustomRequester.send_request(method="post", url)

# @pytest.fixture()
# def json_create_movie():
#         random_name = DataGenerator.generate_name_movies(),
#         random_img = DataGenerator.generate_img_movie(),
#         random_price = DataGenerator.random_price(),
#         random_description = DataGenerator.random_desription(),
#         random_id = DataGenerator.random_id()
#
#         return{
#             "name": random_name,
#             "imageUrl": random_img,
#             "price": random_price,
#             "description":random_description,
#             "location": "SPB",
#             "published": "true",
#             "genreId": random_id
#         }
# @pytest.fixture(scope="session")
# def session():
#     http_session = requests.Session()
#     yield http_session
#     http_session.close()
#
# @pytest.fixture(scope="session")
# def api_manager(session):
#     base_url = BASE_URL
#     return ApiManager(session, base_url)

@pytest.fixture(scope="session")
def session():
    session_auth = requests.Session()
    responce = session_auth.post(url="https://auth.dev-cinescope.coconutqa.ru/login",json={"email":"api1@gmail.com","password":"asdqwe123Q"})
    assert responce.status_code in (201,200), "Статус код не верный"
    token = responce.json().get("accessToken")
    session_auth.headers.update({"Authorization":f"Bearer {token}"})
    yield session_auth
    session_auth.close()

@pytest.fixture(scope="session")
def api_manager(session):
    base_url = BASE_URL
    return ApiManager(session, base_url)