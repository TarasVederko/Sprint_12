import allure
import pytest
from data.data_important_question import Data
from pages.main_page import MainPage


class TestImportantQuestion:

    @pytest.mark.parametrize(('question_locator', 'answer_locator','question_text', 'expected_text'), Data.questions_and_answers)
    @allure.title("Проверяем правильность ответа на вопрос {question_text}")
    def test_answer(self, driver, question_locator, answer_locator, question_text, expected_text):
        page = MainPage(driver)
        page.click_on_element(question_locator)
        result = page.get_text_on_element(answer_locator)
        assert result == expected_text, 'Ошибка в тексте ответа'
