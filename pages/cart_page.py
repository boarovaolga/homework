from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Переход к оформлению заказа
    def go_to_checkout(self):
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
