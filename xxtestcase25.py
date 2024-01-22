from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page_visible(driver):
    assert "Automation Exercise" in driver.title
    print("Step 3: Successfully opened the website")

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Step 4: Scrolled down to bottom")

def verify_subscription_visible(driver):
    subscription_text = "Subscription"  # Replace with the actual text
    subscription_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{subscription_text}')]")
    assert subscription_text in subscription_element.text
    print(f"Step 5: Verified text '{subscription_text}' is visible")

def scroll_upward(driver):
    arrow_button = driver.find_element(By.XPATH, "//div[@class='arrow-right']")
    arrow_button.click()
    print("Step 6: Clicked on the arrow to move upward")

def verify_text_visible(driver, text):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, f"//*[contains(text(), '{text}')]"), text))
        print(f"Step 7: Verified that '{text}' is visible on the screen")
    except TimeoutException:
        print(f"Step 7: '{text}' is not visible on the screen")

def run_test_case():
    try:
        driver = launch_browser()
        navigate_to_url(driver, "http://automationexercise.com")
        verify_home_page_visible(driver)
        scroll_to_bottom(driver)
        verify_subscription_visible(driver)
        scroll_upward(driver)
        verify_text_visible(driver, "Full-Fledged practice website for Automation Engineers")

        print("Test Case: Scroll Down and Up - Passed")
    except Exception as e:
        print(f"Test Case: Scroll Down and Up - Failed. Reason: {str(e)}")
    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
run_test_case()
