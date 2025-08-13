from selenium import webdriver
from LoginPage import LoginPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)

login_page.open_page()
login_page.login("standard_user", "secret_sauce")

if "inventory" in driver.current_url:
    print("✅ from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from LoginPage import LoginPage

def run_test(username, password, expected_result):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        login_page = LoginPage(driver)
        
        login_page.open_page()
        login_page.login(username, password)
        
        if expected_result == "success":
            if "inventory" in driver.current_url:
                print(f"✅ Test Passed for user '{username}'")
            else:
                print(f"❌ Test Failed for user '{username}'")
        else:
            error_msg = login_page.get_error_message()
            print(f"🔴 Error for user '{username}': {error_msg}")
            
    finally:
        driver.quit()

run_test("standard_user", "secret_sauce", "success")
run_test("locked_out_user", "wrong_pass", "fail")
run_test("", "secret_sauce", "fail")Test Passed: Login Successful!")
else:
    print("❌ Test Failed: Login Not Redirected")

driver.quit()

driver = webdriver.Chrome()
login_page = LoginPage(driver)

login_page.open_page()
login_page.login("locked_out_user", "wrong_pass")

error_msg = login_page.get_error_message()
print(f"🔴 Error Message: {error_msg}")

driver.quit()

driver = webdriver.Chrome()
login_page = LoginPage(driver)

login_page.open_page()
login_page.login("", "secret_sauce")

error_msg = login_page.get_error_message()
if "Username is required" in error_msg:
    print("✅ Test Passed: Empty Username Detected")
else:
    print(f"❌ Test Failed: Unexpected Error - {error_msg}")

driver.quit()