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

def verify_brands_visible(driver):
    try:
        brands_sidebar = driver.find_element(By.XPATH, "//div[@class='left-sidebar']")
        assert brands_sidebar.is_displayed()
        print("Step 4: Brands are visible on the left sidebar")
    except AssertionError:
        print("Step 4: Brands are not visible on the left sidebar")

def click_brand(driver, brand_name):
    brand_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{brand_name}')]")
    brand_link.click()

def verify_navigated_to_brand(driver, expected_text):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='brand-title']"), expected_text))
        print(f"Step 6: Navigated to brand page with text '{expected_text}'")
    except TimeoutException:
        print(f"Step 6: Timed out waiting for brand page with text '{expected_text}'")

# Run the test case
try:
    driver = launch_browser()
    navigate_to_url(driver, "http://automationexercise.com")
    click_products_button(driver)
    verify_brands_visible(driver)

    # Replace 'BrandName' with the actual brand name you want to click
    click_brand(driver, "BrandName")
    
    verify_navigated_to_brand(driver, "BrandName")

    # Replace 'AnotherBrand' with the actual brand name you want to click
    click_brand(driver, "AnotherBrand")
    
    verify_navigated_to_brand(driver, "AnotherBrand")
    
    print("Test Case: Navigate to Brands - Passed")
except Exception as e:
    print(f"Test Case: Navigate to Brands - Failed. Reason: {str(e)}")
finally:
    time.sleep(2)  # Adding a short delay before quitting to see the result
    driver.quit()
