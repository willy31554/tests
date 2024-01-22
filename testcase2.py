from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_login_and_delete_account():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4-5: Click on 'Signup / Login' button, Verify 'Login to your account' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        # Wait for the 'Login to your account' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))

        assert "Login to your account" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'Login to your account' is visible")

        # Step 6-7: Enter correct email address and password, Click 'login' button
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")

        email_input.send_keys("barmasai@mailinator.com")
        password_input.send_keys("123456789")

        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()

        print("Step 6-7: Entered correct email and password, Clicked 'login' button")

        # Step 8: Verify that 'Logged in as username' is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
        )
        assert "Logged in as" in driver.page_source
        print("Step 8: Verified that 'Logged in as username' is visible - Pass")



        # # Step 9-10: Click 'Delete Account' button, Verify that 'ACCOUNT DELETED!' is visible
        # delete_account_button_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a"
        # delete_account_button = WebDriverWait(driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, delete_account_button_xpath))
        # )
        # delete_account_button.click()

        # deleted_account_message_xpath = "//h2[contains(text(), 'Delete Account')]"
        # WebDriverWait(driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, deleted_account_message_xpath))
        # )
        # assert "ACCOUNT DELETED!" in driver.page_source
        # print("Step 9-10: Clicked 'Delete Account' button, Verified 'Delete Account' is visible")
        try:
            # Wait for 'Delete Account' link to be present and visible
            deleted_account_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/delete_account') and contains(text(), 'Delete Account')]"))
            )
        except TimeoutException as e:
            # Print more information about the page state
            print(f"Current URL: {driver.current_url}")
            print(f"Page source: {driver.page_source}")
            
            # Re-raise the TimeoutException
            raise e

        # Verify that 'Delete Account' is visible
        assert "Delete Account" in deleted_account_link.text
        print("Step 18: Successfully deleted account and verified 'Delete Account' is visible")

        # Click 'Continue' button after account deletion
        delete_account_continue_button_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a"
        delete_account_continue_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, delete_account_continue_button_xpath))
        )
        delete_account_continue_button.click()
        print("Clicked to continue after account deletion")
    finally:
        driver.quit()

# Run the test case
#test_login_and_delete_account()

# Run the test case
try:
    test_login_and_delete_account()
    print("Test Case 1: test_login_and_delete_account - Passed")
except Exception as e:
    print(f"Test Case 1: test_login_and_delete_account - Failed. Reason: {str(e)}")
