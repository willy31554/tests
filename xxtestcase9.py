from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_search_products():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4-5: Click on 'Products' button
        products_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
        products_button.click()
        print("Step 4-5: Clicked on 'Products' button")

        # Step 6: Verify user is navigated to ALL PRODUCTS page successfully
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("ALL PRODUCTS"))
            print("Title contains 'ALL PRODUCTS'")
        except TimeoutException:
            print(f"Timed out waiting for title. Current title: {driver.title}")

        # Step 7-8: Enter product name in search input and click search button
        search_input = driver.find_element(By.XPATH, "//input[@name='s']")
        search_input.send_keys("Product Name")  # Replace with the actual product name
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()
        print("Step 7-8: Searched for products")

        # Step 9: Verify 'SEARCHED PRODUCTS' is visible
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='SEARCHED PRODUCTS']")))
            print("'SEARCHED PRODUCTS' is visible")
        except TimeoutException:
            print("Timed out waiting for 'SEARCHED PRODUCTS'")

        # Step 10: Verify all the products related to search are visible (you need to modify this based on your webpage structure)
        # Example: Assuming each product is represented by a class 'product-item'
        product_items = driver.find_elements(By.CLASS_NAME, "product-item")
        if product_items:
            print(f"Found {len(product_items)} products related to the search")
        else:
            print("No products found related to the search")

    finally:
        driver.quit()

# Run the test case
try:
    test_search_products()
    print("Test Case: Search Products - Passed")
except Exception as e:
    print(f"Test Case: Search Products - Failed. Reason: {str(e)}")
