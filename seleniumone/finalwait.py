from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time 

class autocart():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://automationexercise.com/products"
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open(self):
        self.driver.get(self.url)
        a = 0
        for i in range(2, 35):
            try:
                product = self.wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/section[2]/div/div/div[2]/div/div[{i}]')))
                actions = ActionChains(self.driver)
                actions.move_to_element(product).perform()
                self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-product-id="{i}"]'))).click()
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button'))).click()
                print(f'Added product {i} successfully')
                a += 1
                time.sleep(1)
            except Exception as e:
                print(f"Failed to add product {i}")
        print(f'The number of items added are: {a}')

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    b = autocart()
    b.open()
    b.quit()