import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoPage:
    """
    Класс для работы со страницей ввода личных данных заказчика.
    Содержит методы для заполнения формы и перехода к следующему шагу.
    """
    def __init__(self, driver):
        """
        Конструктор класса InfoPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение личных данных: {first_name} "
                 "{last_name}, индекс {postal_code}")
    def fill_info(self, first_name: str,
                  last_name: str, postal_code: str) -> None:
        """
        Заполняет форму личных данных (имя, фамилия, почтовый индекс).

        :param first_name: str — имя заказчика.
        :param last_name: str — фамилия заказчика.
        :param postal_code: str — почтовый индекс.
        :return: None
        """

        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажатие кнопки продолжения оформления заказа")
    def continue_checkout(self) -> None:
        """
        Нажимает кнопку "Continue" для перехода к следующему
        этапу оформления заказа.

        :return: None
        """

        self.driver.find_element(By.ID, "continue").click()
