from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://jqueryui.com/selectmenu/')
iframe = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demo-frame")))
driver.switch_to.frame(iframe)

dropdown_button = wait.until(EC.element_to_be_clickable((By.ID, "speed-button")))
dropdown_button.click()
items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul#speed-menu li.ui-menu-item")))

for item in items:
    if item.text.strip() == "Fast":
        item.click()
        break
selected_text = dropdown_button.text
print("Selected option:", selected_text)
driver.switch_to.default_content()

driver.quit()
