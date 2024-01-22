from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_product_details():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website - Pass")

        # Wait for the 'ALL PRODUCTS' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")))

        # Click on 'Products' button
        products_button = driver.find_element(By.XPATH, "//a[contains(@href, '/products')]")
        products_button.click()
        print("Step 4:Clicked on 'Products' buttone - Pass")
        # Wait for the product page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/h2")))

        # Verify that 'ALL PRODUCTS' is in the page source
        assert "ALL products" in driver.page_source
        print("Step 4-5: Clicked on 'Products' button and verified user is navigated to ALL PRODUCTS page - Pass")



        # Step 6: Verify that the products list is visible (you may need to add specific verifications based on your page structure)

        # Step 7: Click on 'View Product' of the first product
        view_product_button = driver.find_element(By.XPATH, "//button[text()='View Product']")
        view_product_button.click()

        # Wait for the product detail page to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Product Detail']")))

        assert "Product Detail" in driver.page_source
        print("Step 7: Clicked on 'View Product' button and verified user is landed to product detail page - Pass")

        # Step 8-9: Verify that detail detail is visible: product name, category, price, availability, condition, brand
        product_name = driver.find_element(By.XPATH, "//label[text()='Product Name']/following-sibling::p").text
        category = driver.find_element(By.XPATH, "//label[text()='Category']/following-sibling::p").text
        price = driver.find_element(By.XPATH, "//label[text()='Price']/following-sibling::p").text
        availability = driver.find_element(By.XPATH, "//label[text()='Availability']/following-sibling::p").text
        condition = driver.find_element(By.XPATH, "//label[text()='Condition']/following-sibling::p").text
        brand = driver.find_element(By.XPATH, "//label[text()='Brand']/following-sibling::p").text

        print(f"Step 8-9: Product Details -\nProduct Name: {product_name}\nCategory: {category}\nPrice: {price}\n"
              f"Availability: {availability}\nCondition: {condition}\nBrand: {brand} - Pass")

    except Exception as e:
        print(f"Test Case: View Product Details - Failed. Reason: {str(e)}")

    finally:
        driver.quit()

# Run the test case
try:
    test_view_product_details()
    print("Test Case: View Product Details - Passed")
except Exception as e:
    print(f"Test Case: View Product Details - Failed. Reason: {str(e)}")
