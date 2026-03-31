import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины интернет-магазина.
    """
    def __init__(self, driver):
        """
        Конструктор класса CartPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Переход на страницу оформления заказа")
    def go_to_checkout(self) -> None:
        """
        Переходит на страницу оформления заказа.
        Сначала открывает корзину, затем нажимает кнопку "Checkout".
        :return: None
        """
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
