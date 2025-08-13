from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://the-internet.herokuapp.com/key_presses")

actions = ActionChains(driver)
actions.key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).perform()
result = wait.until(EC.visibility_of_element_located((By.ID,'result')))
print(result.text)
actions.send_keys(Keys.ARROW_DOWN).perform()
result = wait.until(EC.visibility_of_element_located((By.ID,'result')))
print(result.text)