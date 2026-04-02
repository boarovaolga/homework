import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Lesson_10.pages.cart_page import CartPage
from Lesson_10.pages.info_page import InfoPage
from Lesson_10.pages.login_page import LoginPage
from Lesson_10.pages.product_selection_page import ProductSelectionPage
from Lesson_10.pages.total_amount_page import TotalAmountPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера Firefox.
    :yield: webdriver.Firefox - экземпляр драйвера.
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка оформления заказа")
@allure.description("Тест проверяет полный сценарий покупки: авторизация,"
                    "выбор товара, заполнение данных "
                    "и проверка итоговой суммы.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page(driver) -> None:
    """
    Тест-сценарий полного оформления заказа.
    :param driver: webdriver.Firefox
    :return: None
    """
    with allure.step("Авторизация"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товара в корзину"):
        product_selection_page = ProductSelectionPage(driver)
        product_selection_page.add_items_to_cart(
            ["Sauce Labs Backpack",
             "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        )

    with allure.step("Переход в корзину и оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.go_to_checkout()

    with allure.step("Заполнение персональных данных"):
        info_page = InfoPage(driver)
        info_page.fill_info("Иван", "Петров", "123456")
        info_page.continue_checkout()

    with allure.step("Проверка итоговой суммы"):
        total_amount_page = TotalAmountPage(driver)
        total_amount_page.verify_total_is("Total: $58.29")
