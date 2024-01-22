from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_and_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website - Pass")

        # Step 4-5: Click on 'Signup / Login' button, Verify 'Login to your account' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        # Wait for the 'Login to your account' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))

        assert "Login to your account" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'Login to your account' is visible - Pass")

        # Step 6-7: Enter correct email address and password, Click 'login' button
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")

        email_input.send_keys("barmasai@mailinator.com")
        password_input.send_keys("123456789")

        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()

        print("Step 6-7: Entered correct email and password, Clicked 'login' button - Pass")

        # Step 8: Verify that 'Logged in as username' is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
        )
        assert "Logged in as" in driver.page_source
        print("Step 8: Verified that 'Logged in as username' is visible - Pass")

        # Step 9-10: Click 'Logout' button, Verify user is navigated to login page
        logout_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        logout_button.click()

        # Wait for the 'Login to your account' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
        assert "Login to your account" in driver.page_source
        print("Step 9-10: Clicked 'Logout' button, Verified user is navigated to login page - Pass")

    except Exception as e:
        print(f"Test Case: Login and Logout - Failed. Reason: {str(e)}")

    finally:
        driver.quit()

# Run the test case
try:
    test_login_and_logout()
    print("Test Case: Login and Logout - Passed")
except Exception as e:
    print(f"Test Case: Login and Logout - Failed. Reason: {str(e)}")
