from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/dynamic_loading/1"

driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start"]/button'))).click()

time.sleep(5) 

from selenium.common.exceptions import TimeoutException

try:
    result = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    print(result.text)
except TimeoutException:
    print("Timeout: The 'finish' element did not appear.")
