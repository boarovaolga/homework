import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей авторизации интернет-магазина.
    Содержит методы для открытия страницы и выполнения входа.
    """

    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        :ivar url: str — URL страницы авторизации.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации в онлайн магазине.
        :return: None
        """
        self.driver.get(self.url)

    @allure.step("Заполнение полей авторизации и нажатие кнопки входа")
    def login(self, username: str, password: str) -> None:
        """
        Выполняется вход в систему.
        :param username: str - имя пользователя
        :param password: str - пароль
        :return: None
        """
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
