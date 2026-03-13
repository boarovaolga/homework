import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc_page(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay(45)

    # Выполняем вычисление
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Ожидание результата
    actual_result = calc_page.wait_for_result("15", timeout=50)

    assert actual_result == "15", f"Ожидалось 15, получено {actual_result}"

    print("Тест пройден успешно")
