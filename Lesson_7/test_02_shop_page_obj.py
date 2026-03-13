import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from pages.product_selection_page import ProductSelectionPage
from pages.total_amount_page import TotalAmountPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товара
    product_selection_page = ProductSelectionPage(driver)
    product_selection_page.add_items_to_cart(
        ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    )

    # Переход в корзину
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    # Заполнение персональных данных
    info_page = InfoPage(driver)
    info_page.fill_info("Иван", "Петров", "123456")
    info_page.continue_checkout()

    # Получение итоговой суммы
    total_amount_page = TotalAmountPage(driver)
    total_text = total_amount_page.get_total_text()

    assert total_text == "Total: $58.29", \
        f"Ожидаемая сумма 'Total: $58.29', получена '{total_text}'"

    print("Тест успешно пройден")
