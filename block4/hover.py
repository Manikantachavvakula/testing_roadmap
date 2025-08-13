from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://demoqa.com/menu")

actions = ActionChains(driver)

main_item_2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
actions.move_to_element(main_item_2).perform()


sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
actions.move_to_element(sub_sub_list).perform()

sub_sub_item_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sub Sub Item 1']")))
sub_sub_item_1.click()

wait.until(lambda driver: driver.current_url != "https://demoqa.com/menu")
print("New page URL after click:", driver.current_url)

driver.quit()
