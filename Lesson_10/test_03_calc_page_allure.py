import allure
import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Chrome.
    :yield: webdriver.Chrome — экземпляр драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Тест проверяет, что калькулятор корректно"
                    " выполняет сложение 7 + 8 = 15 с установленной"
                    " задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calc_page(driver):
    """
    Тестовый сценарий для калькулятора с задержкой.
    """
    calc_page = CalcPage(driver)
    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()
    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Проверить результат вычисления"):
        calc_page.verify_result_is("15", timeout=50)
