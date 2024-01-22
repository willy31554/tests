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

def add_products_to_cart(driver):
    # Implement the logic to add products to the cart
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    # for button in add_to_cart_buttons:
    #     button.click()
    print("Step 4: Added products to cart")

def click_cart(driver):
    cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_button.click()
    print("Step 5: Clicked 'Cart' button")

def verify_cart_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Shopping Cart"))
        print("Step 6: Verified cart page is displayed")
    except TimeoutException:
        print("Step 6: Timed out waiting for cart page")

def remove_product_from_cart(driver, product_name):
    # Implement the logic to remove a product from the cart
    # You may need to adjust the XPaths according to your specific webpage structure

    # Example logic (please replace with actual implementation):
    # product_remove_button = driver.find_element(By.XPATH, f"//div[contains(text(), '{product_name}')]/following-sibling::div/button[contains(text(), 'X')]")
    # product_remove_button.click()
    print(f"Step 7: Removed product '{product_name}' from the cart")

def verify_product_removed(driver, product_name):
    try:
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{product_name}')]")))
        print(f"Step 8: Verified product '{product_name}' is removed from the cart")
    except TimeoutException:
        print(f"Step 8: Timed out waiting for product '{product_name}' to be removed")

# Run the test case
try:
    driver = launch_browser()
    navigate_to_url(driver, "http://automationexercise.com")
    verify_home_page(driver)
    add_products_to_cart(driver)
    click_cart(driver)
    verify_cart_page(driver)
    
    # Replace 'Product Name' with the actual name of the product you want to remove
    remove_product_from_cart(driver, "Product Name")
    
    verify_product_removed(driver, "Product Name")
    print("Test Case: Remove Product From Cart - Passed")
except Exception as e:
    print(f"Test Case: Remove Product From Cart - Failed. Reason: {str(e)}")
finally:
    time.sleep(2)  # Adding a short delay before quitting to see the result
    driver.quit()
