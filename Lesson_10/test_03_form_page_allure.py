import allure
import pytest
from selenium import webdriver
from pages.form_page import FormPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Chrome.
    :yield: webdriver.Chrome - экземпляр драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка заполнения и отправки формы")
@allure.description("Тест проверяет, что после заполнения формы "
                    "и её отправки поле 'zip-code' подсвечивается ошибкой,"
                    " а остальные поля — успехом")
@allure.feature("Форма ввода данных")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """
    Тестовый сценарий: открытие формы,
    заполнение, отправка, проверка результатов.
    """
    form_page = FormPage(driver)
    with allure.step("Открыть страницу с формой"):
        form_page.open()
    with allure.step("Заполнить все поля формы данными"):
        form_page.fill_form()
    with allure.step("Отправить форму"):
        form_page.submit_form()
    with allure.step("Проверить результаты заполнения"):
        form_page.check_form_submission()
