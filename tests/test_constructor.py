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
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, TAB_BUNS).get_attribute("class")
        driver.quit()

    def test_tab_sauces(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, TAB_SAUCES).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, TAB_SAUCES).get_attribute("class")
        driver.quit()

    def test_tab_fillings(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(By.XPATH, TAB_FILLINGS).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(By.XPATH, TAB_FILLINGS).get_attribute("class")
        driver.quit()