import allure
from pages.base_page import BasePage
from locators.order_page_locators import FirstPageOrderLocators, SecondPageOrderLocators, ConformationWindows
from locators.main_page_locators import ButtonLocators

class OrderPage(BasePage):

    @allure.step("Заполняем первую страницу в форме заказа и кликаем далее")
    def fill_order_form_page_1(self, name, surname, address, phone):
        self.send_keys_to_input(FirstPageOrderLocators.NAME_FIELD, name)
        self.send_keys_to_input(FirstPageOrderLocators.SURNAME_FIELD, surname)
        self.send_keys_to_input(FirstPageOrderLocators.ADDRESS_FIELD, address)
        self.click_on_element(FirstPageOrderLocators.METRO_STATION_LIST)
        self.click_on_element(FirstPageOrderLocators.METRO_STATION_OPTION)
        self.send_keys_to_input(FirstPageOrderLocators.PHONE_NUMBER_FIELD, phone)
        self.click_on_element(FirstPageOrderLocators.FORWARD_BUTTON)

    @allure.step("Заполняем вторую страницу в форме заказа и кликаем заказать")
    def fill_order_form_page_2(self):
        self.click_on_element(SecondPageOrderLocators.DATE_ORDER_FIELD)
        self.wait_for_element(SecondPageOrderLocators.CALENDAR)
        self.click_on_element(SecondPageOrderLocators.CHOOSE_DATE_ORDER)
        self.click_on_element(SecondPageOrderLocators.PERIOD_ORDER_LIST)
        self.click_on_element(SecondPageOrderLocators.PERIOD_ORDER_TWO_DAYS)
        self.click_on_element(SecondPageOrderLocators.BLACK_COLOR_SCOOTER_CHECKBOX)
        self.click_on_element(ButtonLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Ждем окно подтверждения оформления заказа")
    def confirm_order(self):
        self.wait_for_element(ConformationWindows.YES_BUTTON)
        self.click_on_element(ConformationWindows.YES_BUTTON)
