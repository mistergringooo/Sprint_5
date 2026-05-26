from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from urls import *
from test_data import *

class TestTransitionConstructor:
    def test_transition_via_constructor_button(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(EMAIL)
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(PASSWORD)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_transition_via_logo(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, FIELD_EMAIL).send_keys(EMAIL)
        driver.find_element(By.XPATH, FIELD_PASSWORD).send_keys(PASSWORD)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, LOGO).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL