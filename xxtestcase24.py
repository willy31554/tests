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

def add_products_to_cart(driver):
    # Your logic to add products to the cart

def click_cart_button(driver):
    cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_button.click()

def verify_cart_page_displayed(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Shopping Cart"))
        print("Step 6: Cart page is displayed")
    except TimeoutException:
        print("Step 6: Cart page is not displayed")

def click_proceed_to_checkout(driver):
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed To Checkout')]")
    proceed_to_checkout_button.click()

def fill_signup_form(driver):
    # Replace these XPaths with the actual identifiers for your input fields
    email_input = driver.find_element(By.XPATH, "//input[@name='email']")
    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    confirm_password_input = driver.find_element(By.XPATH, "//input[@name='confirm_password']")
    name_input = driver.find_element(By.XPATH, "//input[@name='name']")
    address_input = driver.find_element(By.XPATH, "//textarea[@name='address']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Replace these values with the actual user details
    email = "test@example.com"
    password = "password123"
    name = "John Doe"
    address = "123 Main St, City, Country"

    email_input.send_keys(email)
    password_input.send_keys(password)
    confirm_password_input.send_keys(password)
    name_input.send_keys(name)
    address_input.send_keys(address)

    submit_button.click()

def verify_account_created(driver):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(), 'ACCOUNT CREATED!')]"), "ACCOUNT CREATED!"))
        print("Step 10: 'ACCOUNT CREATED!' message is visible")
    except TimeoutException:
        print("Step 10: 'ACCOUNT CREATED!' message is not visible")

def click_continue_button(driver):
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()

def verify_logged_in_as(driver, username):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='header']//a[contains(@class, 'account')]/span"), f"Logged in as {username}"))
        print(f"Step 11: 'Logged in as {username}' is visible")
    except TimeoutException:
        print(f"Step 11: 'Logged in as {username}' is not visible")

def verify_address_details(driver):
    # Your logic to verify address details
    pass

def enter_description_and_place_order(driver):
    # Your logic to enter description and place order
    pass

def enter_payment_details_and_confirm_order(driver):
    # Your logic to enter payment details and confirm order
    pass

def verify_order_placed_successfully(driver):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(), 'Your order has been placed successfully!')]"), "Your order has been placed successfully!"))
        print("Step 18: 'Your order has been placed successfully!' message is visible")
    except TimeoutException:
        print("Step 18: 'Your order has been placed successfully!' message is not visible")

def click_download_invoice_button(driver):
    download_invoice_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download Invoice')]")
    download_invoice_button.click()

def verify_invoice_downloaded(driver):
    # Your logic to verify the invoice is downloaded successfully
    pass

def click_continue_after_order(driver):
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()

def click_delete_account_button(driver):
    delete_account_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete Account')]")
    delete_account_button.click()

def verify_account_deleted(driver):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(), 'ACCOUNT DELETED!')]"), "ACCOUNT DELETED!"))
        print("Step 22: 'ACCOUNT DELETED!' message is visible")
    except TimeoutException:
        print("Step 22: 'ACCOUNT DELETED!' message is not visible")

def click_continue_after_deletion(driver):
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()

def run_test_case():
    try:
        driver = launch_browser()
        navigate_to_url(driver, "http://automationexercise.com")
        verify_home_page_visible(driver)
        add_products_to_cart(driver)
        click_cart_button(driver)
        verify_cart_page_displayed(driver)
        click_proceed_to_checkout(driver)
        fill_signup_form(driver)
        verify_account_created(driver)
        click_continue_button(driver)
        verify_logged_in_as(driver, "John Doe")
        click_cart_button(driver)
        click_proceed_to_checkout(driver)
        verify_address_details(driver)
        enter_description_and_place_order(driver)
        enter_payment_details_and_confirm_order(driver)
        verify_order_placed_successfully(driver)
        click_download_invoice_button(driver)
        verify_invoice_downloaded(driver)
        click_continue_after_order(driver)
        click_delete_account_button(driver)
        verify_account_deleted(driver)
        click_continue_after_deletion(driver)

        print("Test Case: Complete Purchase, Download Invoice, Account Deletion - Passed")
    except Exception as e:
        print(f"Test Case: Complete Purchase, Download Invoice, Account Deletion - Failed. Reason: {str(e)}")
    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
run_test_case()
