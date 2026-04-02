import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """
    Класс для работы со страницей формы ввода данных.
    Содержит методы для открытия страницы, заполнения формы,
    отправки и проверки результатов.
    """
    def __init__(self, driver):
        """
        Инициализирует экземпляр FormPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :ivar driver: WebDriver — драйвер браузера.
        :ivar wait: WebDriverWait — объект для явных ожиданий.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields: dict[str, str] = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открыть страницу с формой")
    def open(self) -> None:
        """
        Открывает страницу с формой в браузере.
        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.step("заполнить форму")
    def fill_form(self) -> None:
        """
        Заполнить все поля формы значениями из словаря self.fields.
        :return: None
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Отправить форму")
    def submit_form(self) -> None:
        """
        Нажать на кнопку отправки формы
        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Возвращение значения атрибута")
    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает значение атрибута class элемента по его (id).
        :param field_id: str - идентификатор элемента (id).
        :return: str - строка с классами элемента.
        """""
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверка поля zip-code")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет, что поле zip-code имеет класс alert-danger(ошибка).
        :return: bool - true, если класс alert-danger
        присутствует, иначе False.
        """""
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка обязательных полей")
    def check_fields_success(self) -> bool:
        """
        Проверяет, что все обязательные поля имеют класс success.
        :return: bool - True, если у всех полей
        присутствует класс success, иначе False.
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка заполнения формы")
    def check_form_submission(self) -> None:
        """
        Выполняет проверку корректности заполнения формы.
        Проверяет, что zip-code отмечен ошибкой, а остальные поля - успехом.
        :return: None
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
