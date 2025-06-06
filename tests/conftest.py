import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from curls import *
from locators.main_page_locators import Cookie

@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get(main_site)
    driver.maximize_window()
    driver.find_element(*Cookie.ACCEPT_BUTTON).click()

    yield driver
    driver.quit()