import pytest
import random
import string

def generate_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_part}@yandex.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))