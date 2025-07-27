from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="checkbox-example"]/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox-example"]/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox"]'))).click()

driver.close()