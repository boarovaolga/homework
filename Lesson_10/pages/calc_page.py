import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """
    Класс для работы со страницей калькулятора с задержкой (Slow Calculator).
    Содержит методы для установки задержки, нажатия кнопок,
    получения результата и проверки вычислений.
    """
    def __init__(self, driver):
        """
        Инициализирует экземпляр CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Загрузка страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу в браузере.
        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки: {seconds}")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливаем значение задержки в поле ввода.
        :param seconds: int - время задержки в секундах
        :return: None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажатие на кнопку с текстом: {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажатие на кнопку с заданным текстом.
        :param button_text: str - текст на кнопке (например, '1', '+', '=').
        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//span[text()='{button_text}']"))
        )
        button.click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возвращает текущий текст, отображаемый на экране.
        :return: str - значение, отображаемое на экране
        """
        screen = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen")))
        return screen.text

    @allure.step("Ожидание появления результата: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидает, пока не появиться указанный результат.
        :param expected_result: str - ожидаемое значение.
        :param timeout: int - максимальное время ожидания в секундах
        :return: str - фактический результат после появления
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )
        return self.get_result()

    @allure.step("Проверка результата: {expected}")
    def verify_result_is(self, expected: str, timeout: int = 50) -> None:
        """
        Проверяет, что результат вычисления соответствует ожидаемому.
        Выполняет assert.
        :param expected: str — ожидаемое значение.
        :param timeout: int — максимальное время ожидания в секундах.
        :return: None
        """
        actual = self.wait_for_result(expected, timeout)
        assert actual == expected, f"Ожидалось {expected}, получено {actual}"
