from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from conftest import generate_email, generate_password

class TestRegister:
    def test_successful_register(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, REGISTER_LINK).click()
        driver.find_element(By.XPATH, REGISTER_NAME).send_keys("Антон")
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(generate_password())
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"
        driver.quit()


    def test_incorrect_password(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, REGISTER_LINK).click()
        driver.find_element(By.XPATH, REGISTER_NAME).send_keys("Антон")
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys("anton_test_002@yandex.ru")
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys("12345")
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, INCORRECT_PASSWORD_ERROR).text == "Некорректный пароль"
        driver.quit()