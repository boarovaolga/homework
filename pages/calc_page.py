from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # Открыть страницу
    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    # Установка задержки
    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    # Нажать на кнопку с указанным текстом
    def click_button(self, button_text):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//span[text()='{button_text}']"))
        )
        button.click()

    # Получить текущий результат
    def get_result(self):
        screen = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen")))
        return screen.text

    def wait_for_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )
        return self.get_result()
