from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

def loggstore(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[⏱️] {func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

class waits():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://the-internet.herokuapp.com/dynamic_loading/1"
        self.wait = WebDriverWait(self.driver,timeout = 10)
    
    def launch_site(self):
        self.driver.get(self.url)

    def click_start(self):
        self.driver.find_element(By.XPATH,'//*[@id="start"]/button').click()

    @loggstore
    def wait_and_print_text(self):
        try :
             b =  self.wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="finish"]/h4')))
             print(b.text)
        except TimeoutError : 
            print("Timedout")
    
    def quit(self):
        self.driver.quit()


if __name__ =='__main__':
    print("Practicing waits")
    a = waits()
    a.launch_site()
    a.click_start()
    a.wait_and_print_text()
    a.quit()