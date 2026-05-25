from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestTabs:
    def test_tab_buns(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, SECTION_BUNS)))
        assert driver.find_element(By.XPATH, SECTION_BUNS).is_displayed()
        driver.quit()

    def test_tab_sauces(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, TAB_SAUCES).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, SECTION_SAUCES)))
        assert driver.find_element(By.XPATH, SECTION_SAUCES).is_displayed()
        driver.quit()

    def test_tab_fillings(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, TAB_FILLINGS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, SECTION_FILLINGS)))
        assert driver.find_element(By.XPATH, SECTION_FILLINGS).is_displayed()
        driver.quit()