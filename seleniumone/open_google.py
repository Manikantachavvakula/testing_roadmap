from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

URL = "https://practicetestautomation.com/practice-test-login/"
driver.get(URL)


username = driver.find_element(By.ID, "username")
username.send_keys("student")


password = driver.find_element(By.XPATH, '//input[@id = "password"]')
password.send_keys("Password123")

submit = driver.find_element(By.ID, "submit")
submit.click()

time.sleep(5)

driver.quit()