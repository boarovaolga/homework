import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TotalAmountPage:
    """
    Класс для работы со страницей итоговой суммы заказа.
    Содержит методы для получения итоговой суммы и её проверки.
    """
    def __init__(self, driver):
        """
        Конструктор класса TotalAmountPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Получение итоговой суммы")
    def get_total_text(self) -> str:
        """
        Получает текст итоговой суммы заказа.
        :return: str - текст, содержащий итоговую сумму
        """
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text

    @allure.step("Проверка итоговой суммы: {expected}")
    def verify_total_is(self, expected: str) -> None:
        """
        Проверяет, что итоговая сумма соответствует ожидаемой.
        :param expected: str - ожидаемый текст итоговой суммы.
        :return: None
        """
        actual = self.get_total_text()
        assert actual == expected, (f"Ожидаемая сумма '"
                                    f"{expected}', получена '{actual}'")
