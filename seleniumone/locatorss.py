from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = "https://automationexercise.com/login"
        self.username = "manikanta@123.com"
        self.password = "123456"

    def send_keys(self, css_selector, value):
        """Wrapper to find element by CSS and send keys."""
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        element.send_keys(value)

    def click(self, by_type, value):
        """Wrapper to click any element by locator type."""
        self.driver.find_element(by_type, value).click()

    def loginn(self):
        self.driver.get(self.URL)

        self.send_keys('input[name="email"]', self.username)
        self.send_keys('input[name="password"]', self.password)
        self.click(By.XPATH, "//button[text()='Login']")

        time.sleep(5)

    def add_cart(self):
        self.click(By.XPATH, '//a[@data-product-id="2"]')
        time.sleep(3)
        self.click(By.PARTIAL_LINK_TEXT, "Contact")
        time.sleep(5)

    def homesearch(self):
        self.click(By.LINK_TEXT, "Home")
        time.sleep(3)
        self.send_keys("#search_product", "Tshirt")
        self.click(By.ID, "submit_search")
        time.sleep(5)

test = TestAutomation()
test.loginn()
test.add_cart()
test.homesearch()
