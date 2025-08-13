from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class alerts():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://the-internet.herokuapp.com/javascript_alerts"
        self.wait = WebDriverWait(self.driver,10)

    def jsalert1(self):
        self.driver.get(self.url)
        try : 
            self.driver.find_element(By.XPATH,"//button[normalize-space() = 'Click for JS Alert']").click()
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
            
            result = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//p[@id='result']")))
            print(result.text)
        except TimeoutException :
            print("Element took too long to load")


if __name__ == '__main__' :
    a= alerts()
    a.jsalert1()

