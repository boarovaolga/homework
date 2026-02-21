from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, "input"))
)

input_field.send_keys("Sky")
input_field.clear()
input_field.send_keys("Pro")

sleep(5)
driver.quit()
