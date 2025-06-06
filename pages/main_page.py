import allure
from pages.base_page import BasePage

class MainPage(BasePage):

     @allure.step("Клик на вопрос")
     def click_on_question(self, locator):
         self.click_on_element(locator)

     @allure.step("Проверка ответа")
     def check_answer(self, locator):
         return self.get_text_on_element(locator)





