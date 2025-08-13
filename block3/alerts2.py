from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 

class way2automation():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "http://way2automation.com/way2auto_jquery/frames-and-windows.php#load_box"
        self.wait = WebDriverWait(self.driver,10)

    def alert1(self):
        self.driver.get(self.url)
        try :
            self.wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()  = 'Alert']"))).click()
            frame = self.driver.find_element(By.XPATH,"//iframe[@src='alert/simple-alert.html' ]")
            self.driver.switch_to.frame(frame)
            self.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@onclick='myFunction()']"))).click()
            alert = self.driver.switch_to.alert
            result = alert.text
            print(result)
            alert.accept()
            assert result == "I am an alert box!" , "Alert successfully not handled"
            print("Alert successfully handled!")
        except TimeoutException :
            print("Time out")


if __name__ == '__main__':
    a = way2automation()
    a.alert1()

