import pytest
import random
import string

def generate_email():
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"anton_skryabin_45_{random_digits}@yandex.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))