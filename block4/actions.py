from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains 


class action():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demoqa.com/buttons"
        self.wait = WebDriverWait(self.driver,20)
    
    def clicks(self):
        self.driver.get(self.url)
        try : 
            ele = self.wait.until(EC.visibility_of_element_located((By.ID,"doubleClickBtn")))
            action = ActionChains(self.driver)
            action.double_click(ele).perform()
            txt = self.wait.until(EC.visibility_of_element_located((By.ID,"doubleClickMessage")))
            print(txt.text) 
            ele1 = self.wait.until(EC.visibility_of_element_located((By.ID,"rightClickBtn")))
            action = ActionChains(self.driver)
            action.context_click(ele1).perform()
            txt2 = self.wait.until(EC.visibility_of_element_located((By.ID,"rightClickMessage")))
            print(txt2.text)
            # assert "You have done" in txt and txt1 , 'Failed to click'
            self.driver.quit()
        except TimeoutException :
            print ('Time out')

if __name__ == '__main__':
    a = action()
    a.clicks()