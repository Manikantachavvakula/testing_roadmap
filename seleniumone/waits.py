from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time 

class explict1():
    def __init__ (self): 
        self.driver = webdriver.Chrome()
        self.url = 'https://automationexercise.com/login'
        self.wait = WebDriverWait(self.driver,timeout=10)

    def open(self):
        self.driver.get(self.url)
        try : 
            self.wait.until(EC.visibility_of_element_located((By.NAME,'name')))
            print("Login form loaded successfully")
        except TimeoutError :
            print("Login form not loaded")
    def quit(self):
        self.driver.quit()

class explict2():
        def __init__ (self): 
              self.driver = webdriver.Chrome()
              self.url = 'https://automationexercise.com/products'
              self.wait = WebDriverWait(self.driver,timeout=10)
        def product(self):
            self.driver.get(self.url)

            product = self.driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/img')
            actions = ActionChains(self.driver)
            actions.move_to_element(product).click().perform()
            try :
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='2']")))
                time.sleep(10)
                print("Added to the cart successfully")
            except TimeoutError : 
                print("failed to add to cart")

        def quit(self):
            self.driver.quit()


if __name__ == '__main__':
   print("Practice for explicit")
   a = explict1()
   a.open()
   a.quit()
   print("Adding to cart")
   b=explict2()
   b.product()
   b.quit()