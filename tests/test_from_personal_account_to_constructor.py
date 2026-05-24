from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestTransitionConstructor:
    def test_transition_via_constructor_button(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys("anton_test_003@yandex.ru")
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        driver.quit()

    def test_transition_via_logo(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys("anton_test_003@yandex.ru")
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys("123456")
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, LOGO).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        driver.quit()