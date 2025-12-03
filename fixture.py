import random

import pytest
import requests
from Movies.utils.datagenerator import DataGenerator



@pytest.fixture()
def json_create_movie():

        random_name = DataGenerator.generate_name_movies()
        random_img = DataGenerator.generate_img_movie()
        random_price = DataGenerator.random_price()
        random_description = DataGenerator.random_desription()
        random_id = random.choice([1,3, 8])


        return{
            "name": random_name,
            "imageUrl": random_img,
            "price": random_price,
            "description":random_description,
            "location": "SPB",
            "published": True,
            "genreId": random_id
        }