from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def click_products_button(driver):
    products_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]")
    products_button.click()

def verify_navigated_to_all_products_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("ALL PRODUCTS"))
        print("Step 4: Navigated to ALL PRODUCTS page successfully")
    except TimeoutException:
        print("Step 4: Timed out waiting for ALL PRODUCTS page")

def click_view_product_button(driver):
    view_product_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Product')]")
    view_product_button.click()

def verify_write_your_review_visible(driver):
    try:
        write_your_review_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'Write Your Review')]")
        assert write_your_review_text.is_displayed()
        print("Step 6: 'Write Your Review' is visible")
    except AssertionError:
        print("Step 6: 'Write Your Review' is not visible")

def submit_review(driver, name, email, review):
    name_input = driver.find_element(By.ID, "author")
    email_input = driver.find_element(By.ID, "email")
    review_input = driver.find_element(By.ID, "comment")

    name_input.send_keys(name)
    email_input.send_keys(email)
    review_input.send_keys(review)

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

def verify_success_message(driver):
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Thank you for your review.')]"))
        )
        print("Step 9: Success message 'Thank you for your review.' is visible")
    except TimeoutException:
        print("Step 9: Timed out waiting for success message")

def run_test_case():
    try:
        driver = launch_browser()
        navigate_to_url(driver, "http://automationexercise.com")
        click_products_button(driver)
        verify_navigated_to_all_products_page(driver)
        click_view_product_button(driver)
        verify_write_your_review_visible(driver)

        # Replace 'Your Name', 'your_email@example.com', and 'Your review text.' with actual data
        submit_review(driver, "Your Name", "your_email@example.com", "Your review text.")
        verify_success_message(driver)

        print("Test Case: Submit Review - Passed")
    except Exception as e:
        print(f"Test Case: Submit Review - Failed. Reason: {str(e)}")
    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
run_test_case()
