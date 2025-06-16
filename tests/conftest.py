import pytest
from selenium import webdriver
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
