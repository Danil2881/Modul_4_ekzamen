# from Movies.constants import CREATE_GET_ENDPOINT
# from Movies.Custom_requseter import CustomRequester
# from Movies.fixture import user_login
# from Movies.conftest import json_create_movie
#
#
# class Create_movies(CustomRequester):
#     def __init__(self,session, base_url):
#         super().__init__(session=session,base_url="https://api.dev-cinescope.coconutqa.ru")
#
#     print("Перед вызовом created_movies()")
#
#     def created_movies(self,user_login,base_url,json_create_movies):
#         print("Запуск метода created_movies")
#         responce = user_login.post(url=f"{base_url}{CREATE_GET_ENDPOINT}",json=json_create_movies)
#         assert responce.status_code == 300, f"Unexpected status code: {responce.status_code}"
#         self.id = responce.json().get("id")
#
#     def receiving_movies(self,user_login,base_url):
#         response = user_login.get(url = f"{base_url}{CREATE_GET_ENDPOINT}",json=self.id)
#         assert response.status_code == 200, "не верный статус код при получении"


# Импортируйте необходимые модули
from Movies.constants import CREATE_GET_ENDPOINT
#from Movies.fixture import user_login
from Movies.fixture import json_create_movie
from Movies.Custom_requseter import CustomRequester
from Movies.constants import BASE_URL

# Определите ваш класс
class Create_movies(CustomRequester):
    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=BASE_URL)



    def created_movies(self, json_create_movies):
        print("Начало метода created_movies")  # Отладочный вывод
        responce = self.session.post(url=f"{self.base_url}{CREATE_GET_ENDPOINT}", json = json_create_movies)
        print(f"Ответ статуса: {responce.status_code}")
        assert responce.status_code == 201, f"Unexpected status code: {responce.status_code}"
        self.id = responce.json().get("id")
        print(f"Полученный id: {self.id}")
        return responce

    def receiving_created_movies(self):
        response = self.session.get(url=f"{self.base_url}{CREATE_GET_ENDPOINT}/{self.id}")
        assert response.status_code == 200, "не верный статус код при получении"
        return response


# Основная часть для вызова
if __name__ == "__main__":
    # Создайте сессию или передайте её явно, если нужно
    session = None  # Или инициализируйте как нужно
    base_url = "https://api.dev-cinescope.coconutqa.ru"
    create_movies = Create_movies(session, base_url)

    # Обертка вызова в try/except для диагностики
    try:
        print("Перед вызовом created_movies()")
        create_movies.created_movies(user_login(), base_url, json_create_movie)
        print("После вызова created_movies()")
    except Exception as e:
        import traceback
        print(f"Обнаружено исключение: {e}")
        traceback.print_exc()