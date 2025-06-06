from locators.main_page_locators import QuestionLocators, AnswerQuestionLocators

class Texts:
    QUESTION_TEXT_1 = f'Сколько это стоит? И как оплатить?'
    ANSWER_TEXT_1 = f'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    QUESTION_TEXT_2 = f'Хочу сразу несколько самокатов! Так можно?'
    ANSWER_TEXT_2 = f'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    QUESTION_TEXT_3 = f'Как рассчитывается время аренды?'
    ANSWER_TEXT_3 = f'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    QUESTION_TEXT_4 = f'Можно ли заказать самокат прямо на сегодня?'
    ANSWER_TEXT_4 = f'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    QUESTION_TEXT_5 = f'Можно ли продлить заказ или вернуть самокат раньше?'
    ANSWER_TEXT_5 = f'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    QUESTION_TEXT_6 = f'Вы привозите зарядку вместе с самокатом?'
    ANSWER_TEXT_6 = f'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    QUESTION_TEXT_7 = f'Можно ли отменить заказ?'
    ANSWER_TEXT_7 = f'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    QUESTION_TEXT_8 = f'Я жизу за МКАДом, привезёте?' #грамматическая ошибка в слове живу
    ANSWER_TEXT_8 = f'Да, обязательно. Всем самокатов! И Москве, и Московской области.'



class Data:
    questions_and_answers = [
        (QuestionLocators.QUESTION_1, AnswerQuestionLocators.ANSWER_1, Texts.QUESTION_TEXT_1, Texts.ANSWER_TEXT_1),
        (QuestionLocators.QUESTION_2, AnswerQuestionLocators.ANSWER_2, Texts.QUESTION_TEXT_2, Texts.ANSWER_TEXT_2),
        (QuestionLocators.QUESTION_3, AnswerQuestionLocators.ANSWER_3, Texts.QUESTION_TEXT_3, Texts.ANSWER_TEXT_3),
        (QuestionLocators.QUESTION_4, AnswerQuestionLocators.ANSWER_4, Texts.QUESTION_TEXT_4, Texts.ANSWER_TEXT_4),
        (QuestionLocators.QUESTION_5, AnswerQuestionLocators.ANSWER_5, Texts.QUESTION_TEXT_5, Texts.ANSWER_TEXT_5),
        (QuestionLocators.QUESTION_6, AnswerQuestionLocators.ANSWER_6, Texts.QUESTION_TEXT_6, Texts.ANSWER_TEXT_6),
        (QuestionLocators.QUESTION_7, AnswerQuestionLocators.ANSWER_7, Texts.QUESTION_TEXT_7, Texts.ANSWER_TEXT_7),
        (QuestionLocators.QUESTION_8, AnswerQuestionLocators.ANSWER_8, Texts.QUESTION_TEXT_8, Texts.ANSWER_TEXT_8)
    ]







    name_1 = 'Энакин'
    surname_1 = 'Скайуокер'
    adress_1 = 'Татуин'
    phone_number_1 = '+2162193141'

    name_2 = 'Джа-Джа'
    surname_2 = 'Бинкс'
    adress_2 = 'Набу'
    phone_number_2 = '+4419233141'

    name_3 = 'Лея'
    surname_3 = 'Органа-Соло'
    adress_3 = 'Альдеараан'
    phone_number_3 = "+7531415926"
