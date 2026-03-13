from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductSelectionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Добавление товара по названию
    def add_items_to_cart(self, items_names):
        for item_name in items_names:
            item_xpath = (f"//div[text()='{item_name}']"
                          f"/ancestor::div[@class='inventory_item']"
                          f"//button[text()='Add to cart']")
            add_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, item_xpath))
            )
            add_button.click()
