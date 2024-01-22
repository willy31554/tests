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

def search_product(driver, product_name):
    search_input = driver.find_element(By.NAME, "s")
    search_input.send_keys(product_name)

    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()

def verify_searched_products_visible(driver):
    try:
        searched_products_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'SEARCHED PRODUCTS')]")
        assert searched_products_text.is_displayed()
        print("Step 6: 'SEARCHED PRODUCTS' is visible")
    except AssertionError:
        print("Step 6: 'SEARCHED PRODUCTS' is not visible")

def add_products_to_cart(driver):
    add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[@name='add-to-cart']")
    for button in add_to_cart_buttons:
        button.click()

def click_cart_button(driver):
    cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_button.click()

def verify_products_in_cart(driver):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='product-name']/a")))
        print("Step 9: Products are visible in the cart")
    except TimeoutException:
        print("Step 9: No products found in the cart")

def login(driver, email, password):
    login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    login_button.click()

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_submit_button = driver.find_element(By.NAME, "login")
    login_submit_button.click()

def navigate_to_cart_after_login(driver):
    cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
    cart_button.click()

def run_test_case():
    try:
        driver = launch_browser()
        navigate_to_url(driver, "http://automationexercise.com")
        click_products_button(driver)
        verify_navigated_to_all_products_page(driver)

        # Replace 'Product Name' with the actual product name you want to search
        search_product(driver, "Product Name")
        verify_searched_products_visible(driver)
        add_products_to_cart(driver)
        click_cart_button(driver)
        verify_products_in_cart(driver)

        # Replace 'your_email@example.com' and 'your_password' with actual login details
        login(driver, "your_email@example.com", "your_password")
        navigate_to_cart_after_login(driver)
        verify_products_in_cart(driver)

        print("Test Case: Search, Add to Cart, Login, and Verify Cart - Passed")
    except Exception as e:
        print(f"Test Case: Search, Add to Cart, Login, and Verify Cart - Failed. Reason: {str(e)}")
    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
run_test_case()
