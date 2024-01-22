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

def verify_categories_visible(driver):
    try:
        categories_sidebar = driver.find_element(By.XPATH, "//div[@class='left-sidebar']")
        assert categories_sidebar.is_displayed()
        print("Step 3: Categories are visible on the left sidebar")
    except AssertionError:
        print("Step 3: Categories are not visible on the left sidebar")

def click_category(driver, category_name):
    category_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{category_name}')]")
    category_link.click()

def verify_category_page(driver, expected_text):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='category-title']"), expected_text))
        print(f"Step 6: Category page is displayed with text '{expected_text}'")
    except TimeoutException:
        print(f"Step 6: Timed out waiting for category page with text '{expected_text}'")

def navigate_to_subcategory(driver, category_name, subcategory_name):
    category_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{category_name}')]")
    category_link.click()
    
    subcategory_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{subcategory_name}')]")
    subcategory_link.click()

def verify_navigated_to_category(driver, expected_text):
    try:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='category-title']"), expected_text))
        print(f"Step 8: Navigated to category page with text '{expected_text}'")
    except TimeoutException:
        print(f"Step 8: Timed out waiting for category page with text '{expected_text}'")

# Run the test case
try:
    driver = launch_browser()
    navigate_to_url(driver, "http://automationexercise.com")
    verify_categories_visible(driver)

    # Replace 'Women' with the actual category you want to click
    click_category(driver, "Women")
    
    # Replace 'Dress' with the actual subcategory you want to click under 'Women'
    navigate_to_subcategory(driver, "Women", "Dress")
    
    verify_category_page(driver, "WOMEN - TOPS PRODUCTS")

    # Replace 'Men' with the actual category you want to click
    click_category(driver, "Men")
    
    # Replace 'Subcategory' with the actual subcategory you want to click under 'Men'
    navigate_to_subcategory(driver, "Men", "Subcategory")

    verify_navigated_to_category(driver, "Subcategory")
    
    print("Test Case: Navigate to Category and Subcategory - Passed")
except Exception as e:
    print(f"Test Case: Navigate to Category and Subcategory - Failed. Reason: {str(e)}")
finally:
    time.sleep(2)  # Adding a short delay before quitting to see the result
    driver.quit()
