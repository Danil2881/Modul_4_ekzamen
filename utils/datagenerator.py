import random
import string
from string  import digits

from faker import Faker
faker = Faker()

class DataGenerator:

    @staticmethod
    def generate_email():
        random_string = "".join(random.choice(string.ascii_lowercase + string.digits))
        return f"kek{random_string}@gmail.com"

    @staticmethod
    def generate_name():
        return f"{faker.first_name()} {faker.last_name()}"

    @staticmethod
    def generate_random_password():
        # Гарантируем наличие хотя бы одной буквы и одной цифры

        letters = random.choice(string.ascii_lowercase)
        digits = random.choice(string.digits)

        # Дополняем пароль случайными символами из допустимого набора
        special_charse = "?@#$%^&*!"
        all_chars = letters + digits + special_charse
        remaining_length = random.randint(6, 10)
        remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

        # Перемешиваем пароль для рандомизации
        password = list(letters + digits + remaining_chars)
        random.shuffle(password)

        return ''.join(password)

    @staticmethod
    def generate_name_movies():
        return faker.word()

    @staticmethod
    def generate_img_movie():
        return faker.image_url()

    @staticmethod
    def random_price():
        return faker.random_number()

    @staticmethod
    def random_desription():
        return faker.text()

    @staticmethod
    def random_id():
        return faker.uuid4()