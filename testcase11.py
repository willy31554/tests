from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def test_subscribe_newsletter():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4: Click 'Cart' button
        cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        cart_button.click()
        print("Step 4: Clicked 'Cart' button")

        # Step 5: Scroll down to footer
        action_chains = ActionChains(driver)
        footer = driver.find_element(By.XPATH, "//footer")
        action_chains.move_to_element(footer).perform()
        print("Step 5: Scrolled down to footer")

        # # Step 6: Verify text 'SUBSCRIPTION' in footer
        subscription_text = "Subscription"  # Replace with the actual text
        footer_text_locator = (By.XPATH, "//footer//h2[contains(., 'Subscription')]")
        footer_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(footer_text_locator))

        assert subscription_text.upper() in footer_text.text.strip().upper()
        print(f"Step 6: Verified text '{subscription_text}' in footer")


        # Step 7-8: Enter email address and click arrow button, Verify success message
        email_input = driver.find_element(By.XPATH, "//*[@id='susbscribe_email']")  
        email_input.send_keys("test@example.com")  

        arrow_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
        arrow_button.click()
        print("Step 7: Entered email address and clicked arrow button")

        # Verify success message 'You have been successfully subscribed!'
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]"))
            )
            print("Step 8: Success message is visible")
        except TimeoutException:
            print("Timed out waiting for success message")

    finally:
        time.sleep(2)  
        driver.quit()

# Run the test case
try:
    test_subscribe_newsletter()
    print("Test Case: Subscribe Newsletter - Passed")
except Exception as e:
    print(f"Test Case: Subscribe Newsletter - Failed. Reason: {str(e)}")
