from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

text_element = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)
print(text_element.text)

driver.quit()
