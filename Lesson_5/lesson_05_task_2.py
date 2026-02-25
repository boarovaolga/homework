from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

button_locator = (By.XPATH, "//button[contains(@class, 'btn-primary') "
                            "and text()='Button with Dynamic ID']")
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(button_locator)
)
button.click()
print("Синяя кнопка нажата")

sleep(2)
driver.quit()
