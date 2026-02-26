from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 30)
waiter.until(
EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)


def images_fully_loaded(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) < 4:
        return False
    return all(img.get_attribute("complete") == "true" for img in images)

waiter.until(images_fully_loaded)

images = driver.find_elements(By.TAG_NAME, "img")
third_image_src = images[3].get_attribute("src")
print(third_image_src)

driver.quit()
