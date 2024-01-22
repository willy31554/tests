from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_existing_user_signup():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4-5: Click on 'Signup / Login' button, Verify 'New User Signup!' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        # Wait for the 'New User Signup!' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))

        assert "New User Signup!" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'New User Signup!' is visible")

        # Step 6-7: Enter name and already registered email address
        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")

        name_input.send_keys("Test User")
        email_input.send_keys("barmasai@mailinator.com")

        # Step 8: Click 'Signup' button
        signup_button = driver.find_element(By.XPATH, "//div[@class='signup-form']//button[contains(text(), 'Signup')]")
        signup_button.click()

        # Step 9: Verify error 'Email Address already exist!' is visible
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Email Address already exist!')]"))
        )
        assert "Email Address already exist!" in error_message.text
        print("Step 9: Verified error 'Email Address already exist!' is visible - Pass")


    finally:
        driver.quit()

# Run the test case
try:
    test_existing_user_signup()
    print("Test Case: Existing User Signup - Passed")
except Exception as e:
    print(f"Test Case: Existing User Signup - Failed. Reason: {str(e)}")

