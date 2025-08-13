from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "dropdown"))))
one = dropdown.select_by_visible_text("Option 1")
print(dropdown.first_selected_option.text)
two = dropdown.select_by_value("2")
print(dropdown.first_selected_option.text)

driver.quit()