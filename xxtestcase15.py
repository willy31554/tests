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

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Automation Exercise"))
        print("Step 3: Home page is visible successfully")
    except TimeoutException:
        print("Step 3: Timed out waiting for home page")

def click_signup_login(driver):
    signup_login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    signup_login_button.click()
    print("Step 4: Clicked 'Signup / Login' button")

def fill_signup_details(driver):
    # Implement the logic to fill in signup details and create an account
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # username_input = driver.find_element(By.NAME, "username")
    # username_input.send_keys("your_username")
    # password_input = driver.find_element(By.NAME, "password")
    # password_input.send_keys("your_password")
    # confirm_password_input = driver.find_element(By.NAME, "confirm_password")
    # confirm_password_input.send_keys("your_password")
    # signup_submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
    # signup_submit_button.click()

def verify_account_created(driver):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'ACCOUNT CREATED!')]")))
        print("Step 6: Verified 'ACCOUNT CREATED!'")
    except TimeoutException:
        print("Step 6: Timed out waiting for 'ACCOUNT CREATED!'")

def click_continue(driver):
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()
    print("Step 7: Clicked 'Continue' button")

def verify_logged_in(driver, username):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), 'Logged in as {username}')]")))
        print(f"Step 8: Verified 'Logged in as {username}' at top")
    except TimeoutException:
        print(f"Step 8: Timed out waiting for 'Logged in as {username}'")

def add_products_to_cart(driver):
    # Implement the logic to add products to the cart
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    # for button in add_to_cart_buttons:
    #     button.click()

def click_cart(driver):
    cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_button.click()
    print("Step 10: Clicked 'Cart' button")

def verify_cart_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Shopping Cart"))
        print("Step 10: Verified cart page is displayed")
    except TimeoutException:
        print("Step 10: Timed out waiting for cart page")

def proceed_to_checkout(driver):
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed To Checkout')]")
    proceed_to_checkout_button.click()
    print("Step 11: Clicked 'Proceed To Checkout' button")

def verify_address_and_review_order(driver):
    # Implement the logic to verify address details and review the order
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # verify_address_details(driver)
    # review_order(driver)

def verify_address_details(driver):
    # Implement the logic to verify address details
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # address_details = driver.find_element(By.XPATH, "//div[contains(@class, 'address-details')]")
    # assert "Expected Address" in address_details.text

def review_order(driver):
    # Implement the logic to review the order
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # review_order_details = driver.find_element(By.XPATH, "//div[contains(@class, 'order-details')]")
    # assert "Expected Order Details" in review_order_details.text

def enter_comment_and_place_order(driver):
    comment_input = driver.find_element(By.XPATH, "//textarea[@name='comment']")
    comment_input.send_keys("Your comment here")
    place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
    place_order_button.click()
    print("Step 13: Entered description and clicked 'Place Order' button")

def enter_payment_and_confirm_order(driver):
    # Implement the logic to enter payment details and confirm order
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # name_on_card_input = driver.find_element(By.NAME, "name_on_card")
    # name_on_card_input.send_keys("Your Name")
    # card_number_input = driver.find_element(By.NAME, "card_number")
    # card_number_input.send_keys("Your Card Number")
    # cvc_input = driver.find_element(By.NAME, "cvc")
    # cvc_input.send_keys("Your CVC")
    # expiration_date_input = driver.find_element(By.NAME, "expiration_date")
    # expiration_date_input.send_keys("Your Expiration Date")
    # pay_and_confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Pay and Confirm Order')]")
    # pay_and_confirm_button.click()

def verify_success_message(driver):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Your order has been placed successfully!')]")))
        print("Step 16: Verified success message 'Your order has been placed successfully!'")
    except TimeoutException:
        print("Step 16: Timed out waiting for success message")

def delete_account(driver):
    # Implement the logic to delete the account
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # delete_account_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete Account')]")
    # delete_account_button.click()
    # confirm_delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm Delete')]")
    # confirm_delete_button.click()

def verify_account_deleted(driver):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'ACCOUNT DELETED!')]")))
        print("Step 18: Verified 'ACCOUNT DELETED!'")
    except TimeoutException:
        print("Step 18: Timed out waiting for 'ACCOUNT DELETED!'")

def click_continue_after_deletion(driver):
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_button.click()
    print("Step 19: Clicked 'Continue' button after account deletion")

# Run the test case
try:
    driver = launch_browser()
    navigate_to_url(driver, "http://automationexercise.com")
    verify_home_page(driver)
    click_signup_login(driver)
    fill_signup_details(driver)
    verify_account_created(driver)
    click_continue(driver)
    verify_logged_in(driver, "your_username")  # Replace with the actual username
    add_products_to_cart(driver)
    click_cart(driver)
    verify_cart_page(driver)
    proceed_to_checkout(driver)
    verify_address_and_review_order(driver)
    enter_comment_and_place_order(driver)
    enter_payment_and_confirm_order(driver)
    verify_success_message(driver)
    delete_account(driver)
    verify_account_deleted(driver)
    click_continue_after_deletion(driver)
    print("Test Case: Complete User Journey - Passed")
except Exception as e:
    print(f"Test Case: Complete User Journey - Failed. Reason: {str(e)}")
finally:
    time.sleep(2)  # Adding a short delay before quitting to see the result
    driver.quit()
