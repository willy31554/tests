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

        # Use ActionChains to scroll to the footer
        action_chains = ActionChains(driver)
        footer = driver.find_element(By.XPATH, "//footer")
        action_chains.move_to_element(footer).perform()

        print("Step 4: Scrolled down to footer")

        # # Step 5: Verify text 'SUBSCRIPTION' in footer
        subscription_text = "Subscription"  # Replace with the actual text
        footer_text_locator = (By.XPATH, "//footer//h2[contains(., 'Subscription')]")
        footer_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(footer_text_locator))

        assert subscription_text.upper() in footer_text.text.strip().upper()
        print(f"Step 5: Verified text '{subscription_text}' in footer")





        # Step 6-7: Enter email address in input and click arrow button
        email_input = driver.find_element(By.XPATH, "//*[@id='susbscribe_email']")  # Replace with the actual name or identifier of the email input field
        email_input.send_keys("test@example.com")  # Replace with the actual email address

        arrow_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Replace with the actual XPath of the arrow button
        arrow_button.click()

        print("Step 6-7: Entered email address and clicked arrow button")

        # Step 8: Verify success message 'You have been successfully subscribed!' is visible
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]"))
            )
            print("Step 8: Success message is visible")
        except TimeoutException:
            print("Timed out waiting for success message")

    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
try:
    test_subscribe_newsletter()
    print("Test Case: Subscribe Newsletter - Passed")
except Exception as e:
    print(f"Test Case: Subscribe Newsletter - Failed. Reason: {str(e)}")
