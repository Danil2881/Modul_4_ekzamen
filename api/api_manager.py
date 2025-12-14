from Movies.api.moviesApi import MoviesApi
# from Movies.api.moviesApi import ReceivingApi
import pytest
import requests

class ApiManager:

    def __init__(self,session, base_url):
        self.session = session
        self.movies_api = MoviesApi(session,base_url)




