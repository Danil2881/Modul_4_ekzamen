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