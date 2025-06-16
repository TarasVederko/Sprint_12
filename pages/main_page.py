import allure
from pages.base_page import BasePage
from locators.main_page_locators import ButtonLocators, LogoHeaderLocators

class MainPage(BasePage):

     @allure.step("Клик по кнопке Заказать в шапке")
     def click_order_button_header(self):
         self.click_on_element(ButtonLocators.ORDER_BUTTON_HEADER)

     @allure.step("Клик по кнопке Заказать в середине главной страницы")
     def click_order_button_middle(self):
         self.click_on_element(ButtonLocators.ORDER_BUTTON_MIDDLE)

     @allure.step("Клик по логотипу Яндекса в шапке")
     def click_yandex_logo_header(self):
         self.click_on_element(LogoHeaderLocators.YANDEX)

     @allure.step("Клик по логотипу Самокат в шапке")
     def click_scooter_logo_header(self):
         self.click_on_element(LogoHeaderLocators.SCOOTER)
