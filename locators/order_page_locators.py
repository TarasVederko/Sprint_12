from selenium.webdriver.common.by import By

class FirstPageOrderLocators:
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_LIST = (By.CLASS_NAME, 'select-search__input')
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    FORWARD_BUTTON = (By.XPATH, '//button[text()="Далее"]')


class SecondPageOrderLocators:
    DATE_ORDER_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CHOOSE_DATE_ORDER = (By.XPATH, '//div[class.contains()="25"]')
    PERIOD_ORDER_LIST = (By.XPATH, '//div[text()="* Срок аренды"]')
    PERIOD_ORDER_TWO_DAYS = (By.XPATH, '//div[text()="двое суток"]')
    BLACK_COLOR_SCOOTER_CHECKBOX = (By.XPATH, '//input[@id="black"]')
    GREY_COLOR_SCOOTER_CHECKBOX = (By.XPATH, '//input[@id="grey"]')
    ORDER_BUTTON_IN_FORM = (By.XPATH, '//button[text()="Заказать"]')

class ConformationWindow:
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')

class ConformationWindow:
    CONF_TEXT = (By.XPATH, '//div[text()="Заказ оформлен"]')
