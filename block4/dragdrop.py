from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://jqueryui.com/droppable/')

iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
driver.switch_to.frame(iframe)

source = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space() ='Drag me to my target']")))
target = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='droppable']")))

driver.execute_script("arguments[0].scrollIntoView(true);", target)
action = ActionChains(driver)
action.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)

result = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='droppable']/p[text()='Dropped!']")))
print(result.text)

driver.quit()