import allure
from pages.main_page import MainPage
from locators.main_page_locators import ButtonLocators, LogoHeaderLocators
from curls import *
from locators.order_page_locators import FirstPageOrderLocators

class TestLinksInHeader:

    @allure.title('Проверяем переход на главную страницу по клику на лого Самокат в шапке')
    def test_click_logo_scooter(self,driver):
        page = MainPage(driver)
        page.click_on_element(ButtonLocators.ORDER_BUTTON_HEADER)
        page.wait_for_element(FirstPageOrderLocators.NAME_FIELD)
        page.click_scooter_logo_header()
        assert page.get_current_url(driver) == main_site, 'Ошибка в url'

    @allure.title('Проверяем переход на Дзен по клику на логотип Яндекс в шапке')
    def test_click_logo_yandex(self, driver):
        page = MainPage(driver)
        page.click_on_element(LogoHeaderLocators.YANDEX)
        page.switch_to_new_window()
        page.wait_for_url(dzen_site)
        assert dzen_site in page.get_current_url(driver), 'После клика на лого Яндекса страница дзен не открылась'