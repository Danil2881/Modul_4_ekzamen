from Movies.api.create_movies import Create_movies
from Movies.api.receiving import ReceivingApi
import pytest
import requests

class ApiManager:

    def __init__(self,session, base_url):
        self.session = session
        self.create_movies = Create_movies(session,base_url)
        self.receiving_api = ReceivingApi(session)



