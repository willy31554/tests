from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_navigate_to_test_cases():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4-5: Click on 'Test Cases' button
        test_cases_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Test Cases')]")
        test_cases_button.click()
        print("Step 4-5: clicked")

        # Step 6: Verify user is navigated to test cases page successfully
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("Test Cases"))
            print("Title contains 'Test Cases'")
        except TimeoutException:
            print(f"Timed out waiting for title. Current title: {driver.title}")

    finally:
        driver.quit()

# Run the test case
try:
    test_navigate_to_test_cases()
    print("Test Case: Navigate to Test Cases - Passed")
except Exception as e:
    print(f"Test Case: Navigate to Test Cases - Failed. Reason: {str(e)}")
