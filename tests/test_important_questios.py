import allure
import pytest
from data.data_imoprtant_question import Data
from pages.main_page import MainPage

from tests.conftest import driver


class TestImportantQuestion:
    @pytest.mark.parametrize(('question_locator', 'answer_locator','question_text', 'expected_text'), Data.questions_and_answers)
    @allure.title("Проверка ответа на вопрос {question_text}")
    def test_answer(self, driver, question_locator, answer_locator, question_text, expected_text):
        page = MainPage(driver)
        page.click_on_question(question_locator)
        result = page.check_answer(answer_locator)
        assert result == expected_text