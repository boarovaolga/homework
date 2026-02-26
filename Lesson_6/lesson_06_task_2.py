from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()

WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

print(driver.find_element(By.ID, "updatingButton").text)

driver.quit()
