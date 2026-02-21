from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get(" http://the-internet.herokuapp.com/login")

username_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "username"))
)
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.success"))
)

print("Вы вошли в защищенную зону!")

sleep(5)
driver.quit()
