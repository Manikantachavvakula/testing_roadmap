from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/iframe')

time.sleep(2)  

driver.switch_to.frame('mce_0_ifr')

editor_body = driver.find_element(By.ID, "tinymce")


editor_body.clear()

editor_body.send_keys("text entered")

driver.switch_to.default_content()

print(driver.title)
time.sleep(3)
driver.quit()
