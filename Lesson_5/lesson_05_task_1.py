from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

button_xpath = ("//button[contains(concat(' ', normalize-space(@class), ' '),"
                " ' btn-primary ')]")
button = driver.find_element(By.XPATH, button_xpath)
button.click()
print("Синяя кнопка нажата")

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

sleep(3)
driver.quit()
