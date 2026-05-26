from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from conftest import generate_email, generate_password
from urls import *
from test_data import *

class TestRegister:
    def test_successful_register(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, REGISTER_LINK).click()
        driver.find_element(By.XPATH, REGISTER_NAME).send_keys(NAME)
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(generate_password())
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL


    def test_incorrect_password(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, REGISTER_LINK).click()
        driver.find_element(By.XPATH, REGISTER_NAME).send_keys(NAME)
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(INCORRECT_PASSWORD)
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, INCORRECT_PASSWORD_ERROR).text == "Некорректный пароль"