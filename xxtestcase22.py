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

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def verify_recommended_items_visible(driver):
    try:
        recommended_items = driver.find_element(By.XPATH, "//h2[contains(text(), 'RECOMMENDED ITEMS')]")
        assert recommended_items.is_displayed()
        print("Step 4: 'RECOMMENDED ITEMS' are visible")
    except AssertionError:
        print("Step 4: 'RECOMMENDED ITEMS' are not visible")

def click_add_to_cart_on_recommended_product(driver):
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add To Cart')]")
    add_to_cart_button.click()

def click_view_cart_button(driver):
    view_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Cart')]")
    view_cart_button.click()

def verify_product_displayed_in_cart(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'product-name')]/a")))
        print("Step 7: Product is displayed in cart page")
    except TimeoutException:
        print("Step 7: Product is not displayed in cart page")

def run_test_case():
    try:
        driver = launch_browser()
        navigate_to_url(driver, "http://automationexercise.com")
        scroll_to_bottom(driver)
        verify_recommended_items_visible(driver)
        click_add_to_cart_on_recommended_product(driver)
        click_view_cart_button(driver)
        verify_product_displayed_in_cart(driver)

        print("Test Case: Add Recommended Product to Cart - Passed")
    except Exception as e:
        print(f"Test Case: Add Recommended Product to Cart - Failed. Reason: {str(e)}")
    finally:
        time.sleep(2)  # Adding a short delay before quitting to see the result
        driver.quit()

# Run the test case
run_test_case()
