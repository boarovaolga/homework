import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductSelectionPage:
    """
    Класс для работы со страницей выбора товаров интернет-магазина.
    Содержит методы для добавления товаров в корзину.
    """
    def __init__(self, driver):
        """
        Конструктор класса ProductSelectionPage
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара по названию:  {items_names}")
    def add_items_to_cart(self, items_names: list[str]) -> None:
        """
        Добавляет указанные товары в корзину.
        :param items_names: list[str] - список названий товара для добавления
        :return: None
        """
        for item_name in items_names:
            item_xpath = (f"//div[text()='{item_name}']"
                          f"/ancestor::div[@class='inventory_item']"
                          f"//button[text()='Add to cart']")
            add_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, item_xpath))
            )
            add_button.click()
