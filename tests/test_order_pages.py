import allure
import pytest
from data.data_order_pages import *
from locators.order_page_locators import ConformationWindows
from pages.order_pages import OrderPage
from locators.main_page_locators import ButtonLocators

class TestOrderPageFirst:
    @pytest.mark.parametrize('order_button_locator', [ButtonLocators.ORDER_BUTTON_HEADER, ButtonLocators.ORDER_BUTTON_MIDDLE])
    @pytest.mark.parametrize(('name', 'surname', 'address', 'phone_number'), DataForOrder.data_for_order)
    @allure.title('Проверяем заказ самоката')
    def test_order_scooter(self, driver, order_button_locator, name, surname, address, phone_number):
        page = OrderPage(driver)
        page.click_on_element(order_button_locator)
        page.fill_order_form_page_1(name, surname, address, phone_number)
        page.fill_order_form_page_2()
        page.confirm_order()
        page.wait_for_element(ConformationWindows.CHECK_STATUS_BUTTON)
        result = page.get_text_on_element(ConformationWindows.CONF_TEXT)
        assert 'Заказ оформлен' in result, 'Не удалось оформить заказ'
