from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("https://xyz.com/login")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("correctpass")
    driver.find_element(By.ID, "submit").click()
    assert "Profile" in driver.page_source
    driver.quit()
