from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_shopping_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4: Click 'Products' button
        products_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]")
        products_button.click()
        print("Step 4: Clicked 'Products' button")

        # Step 5: Hover over first product and click 'Add to cart'
        add_to_cart_first_product(driver)
        print("Step 5: Hovered over the first product and clicked 'Add to cart'")

        # Step 6: Click 'Continue Shopping' button
        continue_shopping_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
        continue_shopping_button.click()
        print("Step 6: Clicked 'Continue Shopping' button")

        # Step 7: Hover over second product and click 'Add to cart'
        add_to_cart_second_product(driver)
        print("Step 7: Hovered over the second product and clicked 'Add to cart'")

        # Step 8: Click 'View Cart' button
        view_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Cart')]")
        view_cart_button.click()
        print("Step 8: Clicked 'View Cart' button")

        # Step 9-10: Verify both products in the Cart and their details
        verify_cart(driver)
        print("Step 9-10: Verified both products in the Cart and their details")

    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

def add_to_cart_first_product(driver):
    first_product = driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[2]")
    print("products in the Cart and their details")
    add_to_cart_button = first_product.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[2]")
    print("add in the Cart and their details")
    # Perform a hover over the first product to make 'Add to cart' button visible
    ActionChains(driver).move_to_element(first_product).perform()

    # Click 'Add to cart'
    add_to_cart_button.click()

def add_to_cart_second_product(driver):
    second_product = driver.find_element(By.XPATH, "(//div[@class='product-container'])[2]")
    add_to_cart_button = second_product.find_element(By.XPATH, ".//a[@title='Add to cart']")
    
    # Perform a hover over the second product to make 'Add to cart' button visible
    ActionChains(driver).move_to_element(second_product).perform()

    # Click 'Add to cart'
    add_to_cart_button.click()

def verify_cart(driver):
    # Assuming the products are displayed in a table, adjust the XPaths accordingly
    product_rows = driver.find_elements(By.XPATH, "//table[@id='cart_summary']//tbody/tr")

    # Verify both products are in the Cart
    assert len(product_rows) == 2, "Expected 2 products in the Cart, but found different number."

    # Verify details of the first product
    verify_product_details(product_rows[0], name="Product 1", price="$10.00", quantity="1", total="$10.00")

    # Verify details of the second product
    verify_product_details(product_rows[1], name="Product 2", price="$20.00", quantity="1", total="$20.00")

def verify_product_details(product_row, name, price, quantity, total):
    # Assuming the details are displayed in specific columns, adjust the XPaths accordingly
    name_column = product_row.find_element(By.XPATH, ".//td[@class='cart_description']//p[@class='product-name']")
    price_column = product_row.find_element(By.XPATH, ".//td[@class='cart_unit']//span[@class='price']")
    quantity_column = product_row.find_element(By.XPATH, ".//td[@class='cart_quantity text-center']//input[@class='cart_quantity_input form-control grey']")
    total_column = product_row.find_element(By.XPATH, ".//td[@class='cart_total']//span[@class='price']")
    
    assert name_column.text.strip() == name
    assert price_column.text.strip() == price
    assert quantity_column.get_attribute("value").strip() == quantity
    assert total_column.text.strip() == total

# Run the test case
try:
    test_shopping_cart()
    print("Test Case: Shopping Cart - Passed")
except Exception as e:
    print(f"Test Case: Shopping Cart - Failed. Reason: {str(e)}")
