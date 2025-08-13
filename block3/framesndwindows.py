from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 

class framndwind():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "http://way2automation.com/way2auto_jquery/frames-and-windows.php#load_box"
        self.wait = WebDriverWait(self.driver,10)

    def wind(self):
        self.driver.get(self.url)
        try : 
            self.wait.until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Frames and Windows')]"))).click()
            frame = self.driver.find_element(By.XPATH,"//iframe[@src='frames-windows/defult1.html']")
            self.driver.switch_to.frame(frame)
            original_window = self.driver.current_window_handle
            print(original_window)
            self.wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@target='_blank' and @href = '#']"))).click()
            all_windows = self.driver.window_handles
            for win in all_windows:
              if win != original_window:
                 self.driver.switch_to.window(win)
                 break
            print("New window title:", self.driver.title)
            self.driver.switch_to.window(original_window)
            print("Back to original window title:", self.driver.title)

        except TimeoutException :
            print("Time out")

if __name__ == '__main__':
    a = framndwind()
    a.wind()