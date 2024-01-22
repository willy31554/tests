from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def test_add_product_to_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4: Click 'View Product' for any product on home page
        view_product_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Product')]")
        view_product_button.click()
        print("Step 4: Clicked 'View Product' for the first product")

        # Step 5: Verify product detail is opened
        product_detail_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='product_title']"))
        )
        assert "Product Detail" in product_detail_title.text
        print("Step 5: Verified product detail is opened")

        # Step 6: Increase quantity to 4
        quantity_input = driver.find_element(By.XPATH, "//input[@id='quantity_input']")
        quantity_input.clear()
        quantity_input.send_keys("4")
        print("Step 6: Increased quantity to 4")

        # Step 7: Click 'Add to cart' button
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()
        print("Step 7: Clicked 'Add to cart' button")

        # Step 8: Click 'View Cart' button
        view_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Cart')]")
        view_cart_button.click()
        print("Step 8: Clicked 'View Cart' button")

        # Step 9: Verify that product is displayed in cart page with exact quantity
        verify_product_in_cart(driver, name="Product 1", quantity="4")
        print("Step 9: Verified product in cart with exact quantity")

    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

def verify_product_in_cart(driver, name, quantity):
    # Assuming the product details in the cart are displayed in a table, adjust the XPaths accordingly
    product_row = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//tr[contains(., '{name}')]/td[3][contains(text(), '{quantity}')]"))
    )

    assert product_row is not None, "Product not found in the Cart."

# Run the test case
try:
    test_add_product_to_cart()
    print("Test Case: Add Product to Cart - Passed")
except Exception as e:
    print(f"Test Case: Add Product to Cart - Failed. Reason: {str(e)}")
