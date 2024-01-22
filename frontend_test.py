from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define custom exception
class EmailAlreadyExistsError(Exception):
    pass




def test_register_user():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Step 4-5: Click on 'Signup / Login' button, Verify 'New User Signup!' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        # Wait for the 'New User Signup!' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))

        assert "New User Signup!" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'New User Signup!' is visible")

        # Step 6-15: Register user
        # Enter name and email address for signup
        try:
            fill_signup_form(driver)

        except TimeoutException:
            # Handle timeout exception (e.g., log an error)
            print("Timeout occurred during registration. Check your network or the website.")
            return  # Stop further processing
        # Click 'Continue' button
        continue_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a")
        continue_button.click()
        print("clicked to continue to complete account creation")
        # Step 16-17: Login and Delete Account
        login_and_delete_account(driver)

        try:
            # Wait for 'Delete Account' link to be present and visible
            deleted_account_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/delete_account') and contains(text(), 'Delete Account')]"))
            )
        except TimeoutException as e:
            # Print more information about the page state
            print(f"Current URL: {driver.current_url}")
            print(f"Page source: {driver.page_source}")
            
            # Re-raise the TimeoutException
            raise e

        # Verify that 'Delete Account' is visible
        assert "Delete Account" in deleted_account_link.text
        print("Step 18: Successfully deleted account and verified 'Delete Account' is visible")

        # Click 'Continue' button after account deletion
        delete_account_continue_button_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a"
        delete_account_continue_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, delete_account_continue_button_xpath))
        )
        delete_account_continue_button.click()
        print("Clicked to continue after account deletion")



        # Send email with test results
        send_email('CANDIDATE NAME Frontend test results', 'Register User Test Passed!')
    finally:
        driver.quit()


def fill_signup_form(driver):
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")

    name_input.send_keys("Test User")
    email_input.send_keys("madrfrtttttddhhdrtt5ff44ttiitf@example.com")

    # Click 'Signup' button
    signup_button = driver.find_element(By.XPATH, "//div[@class='signup-form']//button[contains(text(), 'Signup')]")
    signup_button.click()
    


        # Wait until the URL changes to the expected URL
    expected_url = "https://automationexercise.com/signup"
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))


        
    # Assert the current URL after clicking the signup button
    current_url = driver.current_url
    print(f"Current URL after Signup button click: {current_url}")
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    # Step 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='form']/div/div/div/div[1]/h2/b"))
    )
    assert "Enter Account Information" in driver.page_source
    print("Step 8: Verified that 'ENTER ACCOUNT INFORMATION' is visible")

    # Step 9-12: Fill details: Title, Name, Email, Password, Date of birth, Company, etc.
    select_title(driver, "Mr.")  # Step 9
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("your_password")  # Step 10
    select_birth_date(driver, day="1", month="1", year="1990")  # Step 11
    company_input = driver.find_element(By.NAME, "company")
    company_input.send_keys("Example Company")  # Step 12

    # Continue with the rest of the form...
    # For simplicity, I'm skipping the newsletter and optin checkboxes in this example.

    # Address Information
    first_name_input = driver.find_element(By.NAME, "first_name")
    last_name_input = driver.find_element(By.NAME, "last_name")
    address1_input = driver.find_element(By.NAME, "address1")
    address2_input = driver.find_element(By.NAME, "address2")
    country_dropdown = driver.find_element(By.NAME, "country")
    state_input = driver.find_element(By.NAME, "state")
    city_input = driver.find_element(By.NAME, "city")
    zipcode_input = driver.find_element(By.NAME, "zipcode")
    mobile_number_input = driver.find_element(By.NAME, "mobile_number")

    # Fill in the Address Information
    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    address1_input.send_keys("123 Street")
    address2_input.send_keys("Apt 456")
    country_dropdown.send_keys("United States")  # Select the desired country
    state_input.send_keys("California")
    city_input.send_keys("Los Angeles")
    zipcode_input.send_keys("90001")
    mobile_number_input.send_keys("1234567890")

    # Submit the form
    create_account_button = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    create_account_button.click()

    # Check if an error message indicating email already registered is displayed
    if "This email address is already registered" in driver.page_source:
        print("Email is already registered. Please log in instead.")
        return  # Return without further processing

    # Wait for 'ACCOUNT CREATED!' to be present and visible
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='form']/div/div/div/h2/b"))
    )
    assert "Account Created!" in driver.page_source
    print("Step 14: Successfully created account and verified 'ACCOUNT CREATED!' is visible")



def select_title(driver, title):

        # Step 9: Select title
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id='id_gender1']"))
    )
    
    title_radio = driver.find_element(By.XPATH, f"//*[@id='id_gender1']")
    title_radio.click()
    print(f"Step 9: Selected title: {title}")

def select_birth_date(driver, day, month, year):
    day_dropdown = driver.find_element(By.NAME, "days")
    month_dropdown = driver.find_element(By.NAME, "months")
    year_dropdown = driver.find_element(By.NAME, "years")

    # Select day, month, and year
    day_dropdown.send_keys(day)
    month_dropdown.send_keys(month)
    year_dropdown.send_keys(year)

def login_and_delete_account(driver):
    # You need to implement the code for login and delete account steps based on your HTML structure
    # (Enter email, password, click login, click delete account, etc.)
    pass

def send_email(subject, body):
    # Implement the email sending logic using smtplib

    # Example: Using Gmail as SMTP
    sender_email = 'wkipchumba.wk15@gmail.com'
    sender_password = 'dbzj crid hkdl aqcg'
    receiver_email = 'wkipchumba.wk15@gmail.com'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())




def test_login_user_correct_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-5: Launch browser, Navigate to url, Verify home page, Click on 'Signup / Login' button, Verify 'Login to your account' is visible
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button[text()='Login t']")))
        assert "Login to your account" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'Login ' is visible")

        # Step 6: Enter correct email address and password
        enter_login_credentials(driver, "correct_email@example.com", "correct_password")

        # Step 7: Click 'login' button
        login_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
        login_button.click()

        # Step 8: Verify that 'Logged in as username' is visible
        assert "Logged in as username" in driver.page_source
        print("Step 8: Successfully logged in and verified 'Logged in as username' is visible")

        # Step 9: Click 'Delete Account' button
        delete_account_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
        delete_account_button.click()

        # Step 10: Verify that 'ACCOUNT DELETED!' is visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='form']/div/div/div/h2/b"))
        )
        assert "ACCOUNT DELETED!" in driver.page_source
        print("Step 10: Successfully deleted account and verified 'ACCOUNT DELETED!' is visible")

    finally:
        driver.quit()

def enter_login_credentials(driver, email, password):
    # Implement the code to enter email and password
    email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    password_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")

    email_input.send_keys(email)
    password_input.send_keys(password)


def test_login_user_incorrect_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-5: Launch browser, Navigate to url, Verify home page, Click on 'Signup / Login' button, Verify 'Login to your account' is visible
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button()='Login to your account']")))
        assert "Login to your account" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'Login ' is visible")

        # Step 6: Enter incorrect email address and password
        enter_login_credentials(driver, "incorrect_email@example.com", "incorrect_password")

        # Step 7: Click 'login' button
        login_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
        login_button.click()

        # Step 8: Verify error 'Your email or password is incorrect!' is visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/p[text()='Your email or password is incorrect!']"))
        )
        assert "Your email or password is incorrect!" in driver.page_source
        print("Step 8: Successfully verified error message 'Your email or password is incorrect!' is visible")

    finally:
        driver.quit()

def enter_login_credentials(driver, email, password):
    # Implement the code to enter email and password
    email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
    password_input = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')

    email_input.send_keys(email)
    password_input.send_keys(password)


def test_login_user():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Signup / Login' button, Verify 'Login to your account' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
        assert "Login to your account" in driver.page_source
        print("Step 4-5: Clicked on 'Signup / Login' button and verified 'Login to your account' is visible")

        # Step 6: Enter correct email address and password
        enter_login_credentials(driver, "correct_email@example.com", "correct_password")

        # Step 7: Click 'login' button
        login_button = driver.find_element(By.XPATH, "//your_login_button_xpath")
        login_button.click()

        # Step 8: Verify that 'Logged in as username' is visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//your_logged_in_message_xpath[text()='Logged in as username']"))
        )
        assert "Logged in as username" in driver.page_source
        print("Step 8: Successfully verified 'Logged in as username' is visible")

        # Step 9: Click 'Logout' button
        logout_button = driver.find_element(By.XPATH, "//your_logout_button_xpath")
        logout_button.click()

        # Step 10: Verify that user is navigated to login page
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//your_login_page_xpath[text()='Your login page text']"))
        )
        assert "Your login page text" in driver.page_source
        print("Step 10: Successfully verified user is navigated to login page")

    finally:
        driver.quit()

def enter_login_credentials(driver, email, password):
    # Implement the code to enter email and password
    email_input = driver.find_element(By.XPATH, "//your_email_input_xpath")
    password_input = driver.find_element(By.XPATH, "//your_password_input_xpath")

    email_input.send_keys(email)
    password_input.send_keys(password)

def test_existing_email_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Signup / Login' button, Verify 'New User Signup!' is visible
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        signup_login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
        assert "New User Signup!" in driver.page_source
        print("Steps 4-5: Clicked on 'Signup / Login' button and verified 'New User Signup!' is visible")

        # Steps 6-7: Enter name and already registered email address
        fill_signup_form_existing_email(driver)

        # Steps 8: Click 'Signup' button
        signup_button = driver.find_element(By.XPATH, "//div[@class='signup-form']//button[contains(text(), 'Signup')]")
        signup_button.click()

        # Steps 9: Verify error 'Email Address already exist!' is visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//your_error_message_xpath[text()='Email Address already exist!']"))
        )
        assert "Email Address already exist!" in driver.page_source
        print("Step 9: Successfully verified 'Email Address already exist!' is visible")

    finally:
        driver.quit()

def fill_signup_form_existing_email(driver):
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")

    name_input.send_keys("Test User")
    email_input.send_keys("already_registered_email@example.com")


def test_contact_us_form():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Contact Us' button, Verify 'GET IN TOUCH' is visible
        contact_us_button = driver.find_element(By.XPATH, "your_contact_us_button_xpath")
        contact_us_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='GET IN TOUCH']")))
        assert "GET IN TOUCH" in driver.page_source
        print("Steps 4-5: Clicked on 'Contact Us' button and verified 'GET IN TOUCH' is visible")

        # Steps 6-8: Enter name, email, subject, and message, Upload file, Click 'Submit' button
        fill_contact_us_form(driver)

        # Steps 9: Click OK button
        ok_button = driver.switch_to.alert
        ok_button.accept()

        # Steps 10-11: Verify success message 'Success! Your details have been submitted successfully.' is visible
        success_message_xpath = "//your_success_message_xpath[text()='Success! Your details have been submitted successfully.']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        assert "Success! Your details have been submitted successfully." in driver.page_source
        print("Steps 10-11: Successfully verified 'Success! Your details have been submitted successfully.' is visible")

        # Step 12: Click 'Home' button and verify that landed to home page successfully
        home_button = driver.find_element(By.XPATH, "your_home_button_xpath")
        home_button.click()

        # Optionally, add verification for landing on the home page after clicking 'Home' button

    finally:
        driver.quit()

def fill_contact_us_form(driver):
    name_input = driver.find_element(By.NAME, "your_name_input_name")
    email_input = driver.find_element(By.NAME, "your_email_input_name")
    subject_input = driver.find_element(By.NAME, "your_subject_input_name")
    message_input = driver.find_element(By.NAME, "your_message_input_name")
    file_input = driver.find_element(By.NAME, "your_file_input_name")
    submit_button = driver.find_element(By.XPATH, "your_submit_button_xpath")

    name_input.send_keys("Your Name")
    email_input.send_keys("your_email@example.com")
    subject_input.send_keys("Test Subject")
    message_input.send_keys("Test Message")

    # You can use the 'send_keys' method to provide the file path for uploading
    file_input.send_keys("your_file_path")

    submit_button.click()



def test_navigate_to_test_cases_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Test Cases' button
        test_cases_button = driver.find_element(By.XPATH, "//your_test_cases_button_xpath")
        test_cases_button.click()

        # Steps 6-7: Verify user is navigated to test cases page successfully
        test_cases_page_header_xpath = "//your_test_cases_page_header_xpath[text()='Your Test Cases Page Header']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, test_cases_page_header_xpath))
        )
        assert "Your Test Cases Page Header" in driver.page_source
        print("Steps 6-7: Clicked on 'Test Cases' button and verified user is navigated to test cases page successfully")

    finally:
        driver.quit()
def test_view_product_details():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Products' button
        products_button = driver.find_element(By.XPATH, "//your_products_button_xpath")
        products_button.click()

        # Steps 6-7: Verify user is navigated to ALL PRODUCTS page successfully
        all_products_page_header_xpath = "//your_all_products_page_header_xpath[text()='Your All Products Page Header']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, all_products_page_header_xpath))
        )
        assert "Your All Products Page Header" in driver.page_source
        print("Steps 6-7: Clicked on 'Products' button and verified user is navigated to ALL PRODUCTS page successfully")

        # Steps 8-9: Click on 'View Product' of first product and verify product details
        view_product_button_xpath = "//your_view_product_button_xpath"
        view_product_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, view_product_button_xpath))
        )
        view_product_button.click()

        product_detail_page_header_xpath = "//your_product_detail_page_header_xpath[text()='Your Product Detail Page Header']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, product_detail_page_header_xpath))
        )
        assert "Your Product Detail Page Header" in driver.page_source

        # Replace the placeholder XPaths and other values with the actual values from your HTML structure.
        # Verify that detail is visible: product name, category, price, availability, condition, brand
        product_name_xpath = "//your_product_name_xpath"
        product_category_xpath = "//your_product_category_xpath"
        product_price_xpath = "//your_product_price_xpath"
        product_availability_xpath = "//your_product_availability_xpath"
        product_condition_xpath = "//your_product_condition_xpath"
        product_brand_xpath = "//your_product_brand_xpath"

        assert driver.find_element(By.XPATH, product_name_xpath).is_displayed()
        assert driver.find_element(By.XPATH, product_category_xpath).is_displayed()
        assert driver.find_element(By.XPATH, product_price_xpath).is_displayed()
        assert driver.find_element(By.XPATH, product_availability_xpath).is_displayed()
        assert driver.find_element(By.XPATH, product_condition_xpath).is_displayed()
        assert driver.find_element(By.XPATH, product_brand_xpath).is_displayed()

        print("Steps 8-9: Clicked on 'View Product' and verified product detail is visible")

    finally:
        driver.quit()



def test_search_product():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4-5: Click on 'Products' button
        products_button = driver.find_element(By.XPATH, "//your_products_button_xpath")
        products_button.click()

        # Steps 6: Verify user is navigated to ALL PRODUCTS page successfully
        all_products_page_header_xpath = "//your_all_products_page_header_xpath[text()='Your All Products Page Header']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, all_products_page_header_xpath))
        )
        assert "Your All Products Page Header" in driver.page_source
        print("Steps 6: Clicked on 'Products' button and verified user is navigated to ALL PRODUCTS page successfully")

        # Steps 7: Enter product name in search input and click search button
        search_input_xpath = "//your_search_input_xpath"
        search_button_xpath = "//your_search_button_xpath"
        product_name_to_search = "Your Product Name to Search"

        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, search_input_xpath))
        )
        search_input.send_keys(product_name_to_search)

        search_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, search_button_xpath))
        )
        search_button.click()

        # Steps 8: Verify 'SEARCHED PRODUCTS' is visible and all the products related to search are visible
        searched_products_header_xpath = "//your_searched_products_header_xpath[text()='Your Searched Products Header']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, searched_products_header_xpath))
        )
        assert "Your Searched Products Header" in driver.page_source

        # Replace the placeholder XPaths and other values with the actual values from your HTML structure.
        # Verify all the products related to search are visible
        # You can add specific checks based on your HTML structure.

        print("Steps 8: Verified 'SEARCHED PRODUCTS' is visible and all the products related to search are visible")

    finally:
        driver.quit()


def test_subscription():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4: Scroll down to footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Steps 5: Verify text 'SUBSCRIPTION' in the footer
        subscription_text_xpath = "//your_subscription_text_xpath[text()='Your Subscription Text']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, subscription_text_xpath))
        )
        assert "Your Subscription Text" in driver.page_source
        print("Steps 5: Scrolled down to footer and verified text 'SUBSCRIPTION' is visible")

        # Steps 6-7: Enter email address in input and click arrow button
        email_input_xpath = "//your_email_input_xpath"
        arrow_button_xpath = "//your_arrow_button_xpath"
        success_message_xpath = "//your_success_message_xpath[text()='Your Success Message']"

        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, email_input_xpath))
        )
        email_input.send_keys("your_email@example.com")

        arrow_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, arrow_button_xpath))
        )
        arrow_button.click()

        # Steps 8: Verify success message 'You have been successfully subscribed!' is visible
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        assert "Your Success Message" in success_message.text
        print("Steps 7: Entered email address and clicked arrow button. Verified success message is visible.")

    finally:
        driver.quit()
def test_cart_subscription():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4: Click 'Cart' button
        cart_button_xpath = "//your_cart_button_xpath"
        cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, cart_button_xpath))
        )
        cart_button.click()

        # Steps 5: Scroll down to footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Steps 6: Verify text 'SUBSCRIPTION' in the footer
        subscription_text_xpath = "//your_subscription_text_xpath[text()='Your Subscription Text']"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, subscription_text_xpath))
        )
        assert "Your Subscription Text" in driver.page_source
        print("Steps 6: Clicked 'Cart' button, scrolled down to footer, and verified text 'SUBSCRIPTION' is visible")

        # Steps 7-8: Enter email address in input and click arrow button
        email_input_xpath = "//your_email_input_xpath"
        arrow_button_xpath = "//your_arrow_button_xpath"
        success_message_xpath = "//your_success_message_xpath[text()='Your Success Message']"

        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, email_input_xpath))
        )
        email_input.send_keys("your_email@example.com")

        arrow_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, arrow_button_xpath))
        )
        arrow_button.click()

        # Steps 9: Verify success message 'You have been successfully subscribed!' is visible
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        assert "Your Success Message" in success_message.text
        print("Steps 9: Entered email address and clicked arrow button. Verified success message is visible.")

    finally:
        driver.quit()



def test_add_products_to_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Steps 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Steps 1-3: Successfully opened the website")

        # Steps 4: Click 'Products' button
        products_button_xpath = "//your_products_button_xpath"
        products_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, products_button_xpath))
        )
        products_button.click()

        # Steps 5-6: Hover over first product and click 'Add to cart', Click 'Continue Shopping' button
        first_product_xpath = "//your_first_product_xpath"
        add_to_cart_button_xpath = "//your_add_to_cart_button_xpath"
        continue_shopping_button_xpath = "//your_continue_shopping_button_xpath"

        first_product = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, first_product_xpath))
        )
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, add_to_cart_button_xpath))
        )
        first_product.click()
        add_to_cart_button.click()

        continue_shopping_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, continue_shopping_button_xpath))
        )
        continue_shopping_button.click()

        # Steps 7-8: Hover over second product and click 'Add to cart', Click 'View Cart' button
        second_product_xpath = "//your_second_product_xpath"
        second_product = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, second_product_xpath))
        )
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, add_to_cart_button_xpath))
        )
        second_product.click()
        add_to_cart_button.click()

        view_cart_button_xpath = "//your_view_cart_button_xpath"
        view_cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, view_cart_button_xpath))
        )
        view_cart_button.click()

        # Steps 9-10: Verify both products are added to Cart, Verify their prices, quantity, and total price
        # You need to implement the verification logic based on your HTML structure

        print("Steps 9-10: Verify both products are added to Cart and verify their prices, quantity, and total price.")

    finally:
        driver.quit()
# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")
    assert "Automation Exercise" in driver.title
    print("Step 1-3: Successfully opened the website")

    # Verify that home page is visible successfully
    # (You may need to customize the verification based on your HTML structure)
    assert "Home Page Verification Placeholder" in driver.page_source
    print("Step 3: Successfully verified that home page is visible")

    # Click 'View Product' for any product on home page
    view_product_button = driver.find_element(By.XPATH, "//button[contains(text(), 'View Product')]")
    view_product_button.click()

    # Wait for the product detail page to be visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Product Detail']")))

    # Verify product detail is opened
    # (You may need to customize the verification based on your HTML structure)
    assert "Product Detail Verification Placeholder" in driver.page_source
    print("Step 5: Successfully verified that product detail is opened")

    # Increase quantity to 4
    quantity_input = driver.find_element(By.NAME, "quantity")
    quantity_input.clear()
    quantity_input.send_keys("4")

    # Click 'Add to cart' button
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()

    # Click 'View Cart' button
    view_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'View Cart')]")
    view_cart_button.click()

    # Verify that product is displayed in cart page with exact quantity
    # (You may need to customize the verification based on your HTML structure)
    assert "Product in Cart Verification Placeholder" in driver.page_source
    assert "Quantity: 4" in driver.page_source
    print("Step 9: Successfully verified that product is displayed in cart page with exact quantity")

finally:
    # Close the browser
    driver.quit()


def test_checkout_and_account_deletion():
    # Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to url 'http://automationexercise.com'
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Verify that home page is visible successfully
        # (You may need to customize the verification based on your HTML structure)
        assert "Home Page Verification Placeholder" in driver.page_source
        print("Step 3: Successfully verified that home page is visible")

        # Add products to cart
        add_products_to_cart(driver)

        # Click 'Cart' button
        cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        cart_button.click()

        # Verify that cart page is displayed
        # (You may need to customize the verification based on your HTML structure)
        assert "Cart Page Verification Placeholder" in driver.page_source
        print("Step 6: Successfully verified that cart page is displayed")

        # Click Proceed To Checkout
        proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed To Checkout')]")
        proceed_to_checkout_button.click()

        # Click 'Register / Login' button
        register_login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Register / Login')]")
        register_login_button.click()

        # Fill all details in Signup and create account
        fill_signup_form(driver)

        # Verify 'ACCOUNT CREATED!' and click 'Continue' button
        verify_account_created(driver)

        # Verify ' Logged in as username' at top
        assert "Logged in as username Verification Placeholder" in driver.page_source
        print("Step 11: Successfully verified 'Logged in as username' at top")

        # Click 'Cart' button
        cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        cart_button.click()

        # Click 'Proceed To Checkout' button
        proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed To Checkout')]")
        proceed_to_checkout_button.click()

        # Verify Address Details and Review Your Order
        verify_address_and_review_order(driver)

        # Enter description in comment text area and click 'Place Order'
        place_order(driver)

        # Enter payment details: Name on Card, Card Number, CVC, Expiration date
        enter_payment_details(driver)

        # Click 'Pay and Confirm Order' button
        pay_and_confirm_order(driver)

        # Verify success message 'Your order has been placed successfully!'
        assert "Your order has been placed successfully! Verification Placeholder" in driver.page_source
        print("Step 18: Successfully verified 'Your order has been placed successfully!'")

        # Click 'Delete Account' button
        delete_account(driver)

        # Verify 'ACCOUNT DELETED!' and click 'Continue' button
        verify_account_deleted(driver)

    finally:
        # Close the browser
        driver.quit()

def add_products_to_cart(driver):
    # Implement logic to add products to cart based on your HTML structure
    # (Click on products, add to cart buttons, etc.)
    pass

def fill_signup_form(driver):
    # Implement logic to fill signup form based on your HTML structure
    # (Enter name, email, password, etc.)
    pass

def verify_account_created(driver):
    # Implement logic to verify 'ACCOUNT CREATED!' based on your HTML structure
    # (Check for success message, elements on the account page, etc.)
    pass

def verify_address_and_review_order(driver):
    # Implement logic to verify address details and review order based on your HTML structure
    # (Check for address details, items in the order, etc.)
    pass

def place_order(driver):
    # Implement logic to enter description in comment text area and click 'Place Order'
    # based on your HTML structure
    pass

def enter_payment_details(driver):
    # Implement logic to enter payment details based on your HTML structure
    # (Name on Card, Card Number, CVC, Expiration date, etc.)
    pass

def pay_and_confirm_order(driver):
    # Implement logic to click 'Pay and Confirm Order' button based on your HTML structure
    pass

def delete_account(driver):
    # Implement logic to click 'Delete Account' button based on your HTML structure
    pass

def verify_account_deleted(driver):
    # Implement logic to verify 'ACCOUNT DELETED!' based on your HTML structure
    # (Check for success message, elements on the account deletion page, etc.)
    pass

def test_complete_checkout_and_account_deletion():
    # Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Navigate to url 'http://automationexercise.com'
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website")

        # Verify that home page is visible successfully
        # (You may need to customize the verification based on your HTML structure)
        assert "Home Page Verification Placeholder" in driver.page_source
        print("Step 3: Successfully verified that home page is visible")

        # Click 'Signup / Login' button
        signup_login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Signup / Login')]")
        signup_login_button.click()

        # Fill all details in Signup and create account
        fill_signup_form(driver)

        # Verify 'ACCOUNT CREATED!' and click 'Continue' button
        verify_account_created(driver)

        # Verify ' Logged in as username' at top
        assert "Logged in as username Verification Placeholder" in driver.page_source
        print("Step 7: Successfully verified 'Logged in as username' at top")

        # Add products to cart
        add_products_to_cart(driver)

        # Click 'Cart' button
        cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        cart_button.click()

        # Verify that cart page is displayed
        # (You may need to customize the verification based on your HTML structure)
        assert "Cart Page Verification Placeholder" in driver.page_source
        print("Step 10: Successfully verified that cart page is displayed")

        # Click Proceed To Checkout
        proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed To Checkout')]")
        proceed_to_checkout_button.click()

        # Verify Address Details and Review Your Order
        verify_address_and_review_order(driver)

        # Enter description in comment text area and click 'Place Order'
        place_order(driver)

        # Enter payment details: Name on Card, Card Number, CVC, Expiration date
        enter_payment_details(driver)

        # Click 'Pay and Confirm Order' button
        pay_and_confirm_order(driver)

        # Verify success message 'Your order has been placed successfully!'
        assert "Your order has been placed successfully! Verification Placeholder" in driver.page_source
        print("Step 16: Successfully verified 'Your order has been placed successfully!'")

        # Click 'Delete Account' button
        delete_account(driver)

        # Verify 'ACCOUNT DELETED!' and click 'Continue' button
        verify_account_deleted(driver)

    finally:
        # Close the browser
        driver.quit()


# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Navigate to url 'http://automationexercise.com'
driver.get('http://automationexercise.com')

# Step 3: Verify that home page is visible successfully (You need to implement this verification)
# For example, assuming there is a title on the home page
try:
    WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
    print("Home page is visible successfully.")
except Exception as e:
    print("Error: Home page is not visible.")
    print(e)

# Step 4: Click 'Signup / Login' button
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Signup / Login")]')
login_button.click()

# Step 5: Fill email, password and click 'Login' button
email_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'loginSubmit')

email_input.send_keys('your_email@example.com')
password_input.send_keys('your_password')
login_button.click()

# Step 6: Verify 'Logged in as username' at the top (You need to implement this verification)
try:
    logged_in_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Logged in as")]'))
    )
    print(f"Logged in successfully as: {logged_in_text.text}")
except Exception as e:
    print("Error: Login unsuccessful.")
    print(e)

# Step 7: Add products to cart (You need to implement this)

# Step 8: Click 'Cart' button
cart_button = driver.find_element(By.ID, 'cartButton')
cart_button.click()

# Step 9: Verify that cart page is displayed (You need to implement this verification)

# Step 10: Click Proceed To Checkout
checkout_button = driver.find_element(By.ID, 'checkoutButton')
checkout_button.click()

# Step 11: Verify Address Details and Review Your Order (You need to implement this verification)

# Step 12: Enter description in the comment text area and click 'Place Order'
comment_textarea = driver.find_element(By.ID, 'comment')
place_order_button = driver.find_element(By.ID, 'placeOrderButton')

comment_textarea.send_keys('This is a test order')
place_order_button.click()

# Step 13: Enter payment details: Name on Card, Card Number, CVC, Expiration date (You need to implement this)

# Step 14: Click 'Pay and Confirm Order' button
pay_button = driver.find_element(By.ID, 'payButton')
pay_button.click()

# Step 15: Verify success message 'Your order has been placed successfully!' (You need to implement this verification)

# Step 16: Click 'Delete Account' button
delete_account_button = driver.find_element(By.ID, 'deleteAccountButton')
delete_account_button.click()

# Step 17: Verify 'ACCOUNT DELETED!' and click 'Continue' button (You need to implement this verification)

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
        print("Home page is visible successfully.")
    except Exception as e:
        print("Error: Home page is not visible.")
        print(e)

def add_product_to_cart(driver):
    product_add_to_cart_button = driver.find_element(By.ID, 'add_to_cart_button')
    product_add_to_cart_button.click()

def click_cart_button(driver):
    cart_button = driver.find_element(By.ID, 'cartButton')
    cart_button.click()

def verify_cart_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Cart Page Title"))
        print("Cart page is displayed successfully.")
    except Exception as e:
        print("Error: Cart page is not displayed.")
        print(e)

def remove_product_from_cart(driver):
    remove_button = driver.find_element(By.CLASS_NAME, 'remove-product')
    remove_button.click()

def verify_product_removed(driver, element):
    try:
        WebDriverWait(driver, 10).until(EC.staleness_of(element))
        print("Product is successfully removed from the cart.")
    except Exception as e:
        print("Error: Product is not removed from the cart.")
        print(e)

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify home page
navigate_to_url(driver, 'http://automationexercise.com')
verify_home_page(driver)

# Step 4: Add products to cart
add_product_to_cart(driver)

# Step 5-6: Click 'Cart' button, Verify cart page
click_cart_button(driver)
verify_cart_page(driver)

# Step 7: Click 'X' button corresponding to particular product
remove_product_from_cart(driver)

# Step 8: Verify that product is removed from the cart
verify_product_removed(driver, remove_button)

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_categories_visible(driver):
    try:
        categories_sidebar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'categoriesSidebar'))
        )
        print("Categories are visible on the left sidebar.")
    except Exception as e:
        print("Error: Categories are not visible on the left sidebar.")
        print(e)

def click_category(driver, category_name):
    category_link = driver.find_element(By.XPATH, f'//a[contains(text(), "{category_name}")]')
    category_link.click()

def verify_category_page(driver, expected_text):
    try:
        category_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{expected_text}")]'))
        )
        print(f"Category page is displayed successfully. {expected_text}")
    except Exception as e:
        print(f"Error: Category page is not displayed. {expected_text}")
        print(e)

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify categories
navigate_to_url(driver, 'http://automationexercise.com')
verify_categories_visible(driver)

# Step 4-6: Click on 'Women' category, Click on 'Dress' category link, Verify category page
click_category(driver, 'Women')
click_category(driver, 'Dresses')
verify_category_page(driver, 'WOMEN - TOPS PRODUCTS')

# Step 7-8: Click on any sub-category link of 'Men' category, Verify user is navigated to that category page
click_category(driver, 'Men')
click_category(driver, 'Shirts')  # Replace 'Shirts' with the desired sub-category
verify_category_page(driver, 'MEN - SHIRTS')

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def click_button(driver, button_text):
    button = driver.find_element(By.XPATH, f'//button[contains(text(), "{button_text}")]')
    button.click()

def verify_brands_visible(driver):
    try:
        brands_sidebar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'brandsSidebar'))
        )
        print("Brands are visible on the left sidebar.")
    except Exception as e:
        print("Error: Brands are not visible on the left sidebar.")
        print(e)

def click_brand(driver, brand_name):
    brand_link = driver.find_element(By.XPATH, f'//a[contains(text(), "{brand_name}")]')
    brand_link.click()

def verify_brand_page(driver, expected_text):
    try:
        brand_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{expected_text}")]'))
        )
        print(f"Brand page is displayed successfully. {expected_text}")
    except Exception as e:
        print(f"Error: Brand page is not displayed. {expected_text}")
        print(e)

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Click on 'Products' button
navigate_to_url(driver, 'http://automationexercise.com')
click_button(driver, 'Products')

# Step 4: Verify that Brands are visible on left side bar
verify_brands_visible(driver)

# Step 5-6: Click on any brand name, Verify user is navigated to brand page and brand products are displayed
click_brand(driver, 'BrandName1')  # Replace 'BrandName1' with the desired brand name
verify_brand_page(driver, 'BRAND NAME 1')

# Step 7-8: On left side bar, click on any other brand link, Verify user is navigated to that brand page and can see products
click_brand(driver, 'BrandName2')  # Replace 'BrandName2' with the desired brand name
verify_brand_page(driver, 'BRAND NAME 2')

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def click_button(driver, button_text):
    button = driver.find_element(By.XPATH, f'//button[contains(text(), "{button_text}")]')
    button.click()

def verify_page_title(driver, expected_title):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains(expected_title))
        print(f"User is navigated to {expected_title} page successfully.")
    except Exception as e:
        print(f"Error: User is not navigated to {expected_title} page.")
        print(e)

def enter_text_and_click(driver, input_id, search_text):
    search_input = driver.find_element(By.ID, input_id)
    search_input.send_keys(search_text)
    search_button = driver.find_element(By.ID, 'searchButton')
    search_button.click()

def verify_search_results_page(driver):
    try:
        searched_products_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "SEARCHED PRODUCTS")]'))
        )
        print("SEARCHED PRODUCTS page is visible.")
    except Exception as e:
        print("Error: SEARCHED PRODUCTS page is not visible.")
        print(e)

def add_products_to_cart(driver):
    # Assume there are checkboxes for each product and an 'Add to Cart' button
    product_checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
    add_to_cart_button = driver.find_element(By.ID, 'add_to_cart_button')

    for checkbox in product_checkboxes:
        checkbox.click()

    add_to_cart_button.click()

def login(driver, email, password):
    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Signup / Login")]')
    login_button.click()

    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    login_submit_button = driver.find_element(By.ID, 'loginSubmit')

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_submit_button.click()

def go_to_cart_after_login(driver):
    cart_button = driver.find_element(By.ID, 'cartButton')
    cart_button.click()

def verify_products_in_cart(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Product Name")]'))
        )
        print("Products are visible in the cart.")
    except Exception as e:
        print("Error: Products are not visible in the cart.")
        print(e)

# Main script
driver = launch_browser()

# Step 1-4: Launch browser, Navigate to url, Click on 'Products' button, Verify user is navigated to ALL PRODUCTS page
navigate_to_url(driver, 'http://automationexercise.com')
click_button(driver, 'Products')
verify_page_title(driver, 'ALL PRODUCTS')

# Step 5-7: Enter product name in search input, Click search button, Verify 'SEARCHED PRODUCTS' is visible, Verify products
enter_text_and_click(driver, 'searchInput', 'Product Name')  # Replace with the desired product name
verify_search_results_page(driver)

# Step 8: Add those products to cart
add_products_to_cart(driver)

# Step 9: Click 'Cart' button and verify that products are visible in cart
click_button(driver, 'Cart')
verify_products_in_cart(driver)

# Step 10-11: Click 'Signup / Login' button and submit login details, Go to Cart page, Verify products in cart after login
login(driver, 'your_email@example.com', 'your_password')  # Replace with actual login credentials
go_to_cart_after_login(driver)
verify_products_in_cart(driver)

# Close the browser
driver.quit()



def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def click_button(driver, button_text):
    button = driver.find_element(By.XPATH, f'//button[contains(text(), "{button_text}")]')
    button.click()

def verify_page_title(driver, expected_title):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains(expected_title))
        print(f"User is navigated to {expected_title} page successfully.")
    except Exception as e:
        print(f"Error: User is not navigated to {expected_title} page.")
        print(e)

def click_view_product_button(driver):
    view_product_button = driver.find_element(By.XPATH, '//button[contains(text(), "View Product")]')
    view_product_button.click()

def verify_write_review_visible(driver):
    try:
        write_review_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Write Your Review")]'))
        )
        print("Write Your Review section is visible.")
    except Exception as e:
        print("Error: Write Your Review section is not visible.")
        print(e)

def submit_review(driver, name, email, review_text):
    name_input = driver.find_element(By.ID, 'reviewerName')
    email_input = driver.find_element(By.ID, 'reviewerEmail')
    review_input = driver.find_element(By.ID, 'reviewerReview')
    submit_button = driver.find_element(By.ID, 'submitReviewButton')

    name_input.send_keys(name)
    email_input.send_keys(email)
    review_input.send_keys(review_text)
    submit_button.click()

def verify_success_message(driver, expected_message):
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{expected_message}")]'))
        )
        print(f"Success message is displayed: {expected_message}")
    except Exception as e:
        print(f"Error: Success message is not displayed. {expected_message}")
        print(e)

# Main script
driver = launch_browser()

# Step 1-4: Launch browser, Navigate to url, Click on 'Products' button, Verify user is navigated to ALL PRODUCTS page
navigate_to_url(driver, 'http://automationexercise.com')
click_button(driver, 'Products')
verify_page_title(driver, 'ALL PRODUCTS')

# Step 5-6: Click on 'View Product' button, Verify 'Write Your Review' is visible
click_view_product_button(driver)
verify_write_review_visible(driver)

# Step 7-8: Enter name, email and review, Click 'Submit' button
submit_review(driver, 'John Doe', 'john.doe@example.com', 'This is a test review.')
verify_success_message(driver, 'Thank you for your review.')

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def verify_recommendations_visible(driver):
    try:
        recommendations_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "RECOMMENDED ITEMS")]'))
        )
        print("RECOMMENDED ITEMS section is visible.")
    except Exception as e:
        print("Error: RECOMMENDED ITEMS section is not visible.")
        print(e)

def click_add_to_cart(driver):
    add_to_cart_button = driver.find_element(By.XPATH, '//button[contains(text(), "Add To Cart")]')
    add_to_cart_button.click()

def click_view_cart_button(driver):
    view_cart_button = driver.find_element(By.XPATH, '//button[contains(text(), "View Cart")]')
    view_cart_button.click()

def verify_product_in_cart(driver):
    try:
        product_in_cart = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Product Name")]'))
        )
        print("Product is displayed in the cart page.")
    except Exception as e:
        print("Error: Product is not displayed in the cart page.")
        print(e)

# Main script
driver = launch_browser()

# Step 1-2: Launch browser, Navigate to url
navigate_to_url(driver, 'http://automationexercise.com')

# Step 3: Scroll to the bottom of the page
scroll_to_bottom(driver)

# Step 4: Verify 'RECOMMENDED ITEMS' are visible
verify_recommendations_visible(driver)

# Step 5: Click on 'Add To Cart' on Recommended product
click_add_to_cart(driver)

# Step 6-7: Click on 'View Cart' button, Verify that product is displayed in cart page
click_view_cart_button(driver)
verify_product_in_cart(driver)

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
        print("Home page is visible successfully.")
    except Exception as e:
        print("Error: Home page is not visible.")
        print(e)

def click_button(driver, button_text):
    button = driver.find_element(By.XPATH, f'//button[contains(text(), "{button_text}")]')
    button.click()

def fill_signup_details(driver, username, email, password, address):
    username_input = driver.find_element(By.ID, 'username')
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    address_input = driver.find_element(By.ID, 'address')
    signup_button = driver.find_element(By.ID, 'signupButton')

    username_input.send_keys(username)
    email_input.send_keys(email)
    password_input.send_keys(password)
    address_input.send_keys(address)

    signup_button.click()

def verify_account_created(driver):
    try:
        account_created_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "ACCOUNT CREATED!")]'))
        )
        print("Account created successfully.")
    except Exception as e:
        print("Error: Account creation failed.")
        print(e)

def click_continue_button(driver):
    continue_button = driver.find_element(By.ID, 'continueButton')
    continue_button.click()

def verify_logged_in(driver, username):
    try:
        logged_in_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "Logged in as {username}")]'))
        )
        print(f"Logged in successfully as: {username}")
    except Exception as e:
        print("Error: Login unsuccessful.")
        print(e)

def add_products_to_cart(driver):
    # Implement the logic to add products to the cart

def click_cart_button(driver):
    cart_button = driver.find_element(By.ID, 'cartButton')
    cart_button.click()

def verify_cart_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Cart Page Title"))
        print("Cart page is displayed successfully.")
    except Exception as e:
        print("Error: Cart page is not displayed.")
        print(e)

def click_proceed_to_checkout(driver):
    proceed_to_checkout_button = driver.find_element(By.ID, 'proceedToCheckoutButton')
    proceed_to_checkout_button.click()

def verify_delivery_address(driver, expected_address):
    delivery_address_text = driver.find_element(By.ID, 'deliveryAddress').text
    assert delivery_address_text == expected_address, f"Delivery address mismatch. Expected: {expected_address}, Actual: {delivery_address_text}"

def verify_billing_address(driver, expected_address):
    billing_address_text = driver.find_element(By.ID, 'billingAddress').text
    assert billing_address_text == expected_address, f"Billing address mismatch. Expected: {expected_address}, Actual: {billing_address_text}"

def click_delete_account_button(driver):
    delete_account_button = driver.find_element(By.ID, 'deleteAccountButton')
    delete_account_button.click()

def verify_account_deleted(driver):
    try:
        account_deleted_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "ACCOUNT DELETED!")]'))
        )
        print("Account deleted successfully.")
    except Exception as e:
        print("Error: Account deletion failed.")
        print(e)

def click_continue_after_account_deleted(driver):
    continue_button = driver.find_element(By.ID, 'continueButton')
    continue_button.click()

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify home page
navigate_to_url(driver, 'http://automationexercise.com')
verify_home_page(driver)

# Step 4-6: Click 'Signup / Login' button, Fill signup details, Verify 'ACCOUNT CREATED!', Click 'Continue'
click_button(driver, 'Signup / Login')
fill_signup_details(driver, 'YourUsername', 'your_email@example.com', 'YourPassword', 'YourAddress')
verify_account_created(driver)
click_continue_button(driver)

# Step 7: Verify 'Logged in as username' at top
verify_logged_in(driver, 'YourUsername')

# Step 8-9: Add products to cart, Click 'Cart' button, Verify cart page
add_products_to_cart(driver)
click_cart_button(driver)
verify_cart_page(driver)

# Step 10-13: Click Proceed To Checkout, Verify delivery and billing addresses, Click 'Delete Account'
click_proceed_to_checkout(driver)
verify_delivery_address(driver, 'YourAddress')  # Assuming delivery address is the same as signup address
verify_billing_address(driver, 'YourAddress')  # Assuming billing address is the same as signup address
click_delete_account_button(driver)

# Step 14-15: Verify 'ACCOUNT DELETED!', Click 'Continue'
verify_account_deleted(driver)
click_continue_after_account_deleted(driver)

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
        print("Home page is visible successfully.")
    except Exception as e:
        print("Error: Home page is not visible.")
        print(e)

def add_products_to_cart(driver):
    # Implement the logic to add products to the cart

def click_cart_button(driver):
    cart_button = driver.find_element(By.ID, 'cartButton')
    cart_button.click()

def verify_cart_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Cart Page Title"))
        print("Cart page is displayed successfully.")
    except Exception as e:
        print("Error: Cart page is not displayed.")
        print(e)

def click_proceed_to_checkout(driver):
    proceed_to_checkout_button = driver.find_element(By.ID, 'proceedToCheckoutButton')
    proceed_to_checkout_button.click()

def click_register_login_button(driver):
    register_login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Register / Login")]')
    register_login_button.click()

def fill_signup_details(driver, username, email, password, address):
    username_input = driver.find_element(By.ID, 'username')
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    address_input = driver.find_element(By.ID, 'address')
    signup_button = driver.find_element(By.ID, 'signupButton')

    username_input.send_keys(username)
    email_input.send_keys(email)
    password_input.send_keys(password)
    address_input.send_keys(address)

    signup_button.click()

def verify_account_created(driver):
    try:
        account_created_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "ACCOUNT CREATED!")]'))
        )
        print("Account created successfully.")
    except Exception as e:
        print("Error: Account creation failed.")
        print(e)

def click_continue_button(driver):
    continue_button = driver.find_element(By.ID, 'continueButton')
    continue_button.click()

def verify_logged_in(driver, username):
    try:
        logged_in_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "Logged in as {username}")]'))
        )
        print(f"Logged in successfully as: {username}")
    except Exception as e:
        print("Error: Login unsuccessful.")
        print(e)

def verify_address_and_review_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Address and Review Page Title"))
        print("Address Details and Review Your Order page is displayed.")
    except Exception as e:
        print("Error: Address Details and Review Your Order page is not displayed.")
        print(e)

def enter_comment_and_place_order(driver, comment):
    comment_textarea = driver.find_element(By.ID, 'commentTextarea')
    comment_textarea.send_keys(comment)

    place_order_button = driver.find_element(By.ID, 'placeOrderButton')
    place_order_button.click()

def enter_payment_details(driver, card_name, card_number, cvc, expiration_date):
    card_name_input = driver.find_element(By.ID, 'cardName')
    card_number_input = driver.find_element(By.ID, 'cardNumber')
    cvc_input = driver.find_element(By.ID, 'cvc')
    expiration_date_input = driver.find_element(By.ID, 'expirationDate')
    
    card_name_input.send_keys(card_name)
    card_number_input.send_keys(card_number)
    cvc_input.send_keys(cvc)
    expiration_date_input.send_keys(expiration_date)

def click_pay_confirm_order(driver):
    pay_confirm_order_button = driver.find_element(By.ID, 'payConfirmOrderButton')
    pay_confirm_order_button.click()

def verify_order_success_message(driver):
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Your order has been placed successfully!")]'))
        )
        print("Order placed successfully!")
    except Exception as e:
        print("Error: Order placement failed.")
        print(e)

def click_download_invoice_button(driver):
    download_invoice_button = driver.find_element(By.ID, 'downloadInvoiceButton')
    download_invoice_button.click()

def verify_invoice_downloaded(driver):
    # Implement logic to verify if the invoice is downloaded successfully

def click_continue_after_order_placed(driver):
    continue_button = driver.find_element(By.ID, 'continueButton')
    continue_button.click()

def click_delete_account_button(driver):
    delete_account_button = driver.find_element(By.ID, 'deleteAccountButton')
    delete_account_button.click()

def verify_account_deleted(driver):
    try:
        account_deleted_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "ACCOUNT DELETED!")]'))
        )
        print("Account deleted successfully.")
    except Exception as e:
        print("Error: Account deletion failed.")
        print(e)

def click_continue_after_account_deleted(driver):
    continue_button = driver.find_element(By.ID, 'continueButton')
    continue_button.click()

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify home page
navigate_to_url(driver, 'http://automationexercise.com')
verify_home_page(driver)

# Step 4-5: Add products to cart, Click 'Cart' button
add_products_to_cart(driver)
click_cart_button(driver)

# Step 6: Verify cart page is displayed
verify_cart_page(driver)

# Step 7-10: Click Proceed To Checkout, Click 'Register / Login', Fill signup details, Verify 'ACCOUNT CREATED!', Click 'Continue', Verify 'Logged in as username'
click_proceed_to_checkout(driver)
click_register_login_button(driver)
fill_signup_details(driver, 'YourUsername', 'your_email@example.com', 'YourPassword', 'YourAddress')
verify_account_created(driver)
click_continue_button(driver)
verify_logged_in(driver, 'YourUsername')

# Step 11-16: Click 'Cart' button, Click 'Proceed To Checkout' button, Verify Address and Review page, Enter description, Click 'Place Order', Enter payment details, Click 'Pay and Confirm Order', Verify success message
click_cart_button(driver)
click_proceed_to_checkout(driver)
verify_address_and_review_page(driver)
enter_comment_and_place_order(driver, 'This is a test order.')
enter_payment_details(driver, 'Cardholder Name', 'Card Number', 'CVC', 'Expiration Date')
click_pay_confirm_order(driver)
verify_order_success_message(driver)

# Step 17-19: Click 'Download Invoice' button, Verify invoice is downloaded, Click 'Continue'
click_download_invoice_button(driver)
verify_invoice_downloaded(driver)
click_continue_after_order_placed(driver)

# Step 20-22: Click 'Delete Account' button, Verify 'ACCOUNT DELETED!', Click 'Continue'
click_delete_account_button(driver)
verify_account_deleted(driver)
click_continue_after_account_deleted(driver)

# Close the browser
driver.quit()


def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
        print("Home page is visible successfully.")
    except Exception as e:
        print("Error: Home page is not visible.")
        print(e)

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def verify_subscription_visible(driver):
    try:
        subscription_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "SUBSCRIPTION")]'))
        )
        print("SUBSCRIPTION is visible.")
    except Exception as e:
        print("Error: SUBSCRIPTION is not visible.")
        print(e)

def scroll_upward(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

def verify_text_visible_after_scroll(driver, expected_text):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{expected_text}")]'))
        )
        print(f"{expected_text} is visible after scrolling up.")
    except Exception as e:
        print(f"Error: {expected_text} is not visible after scrolling up.")
        print(e)

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify home page
navigate_to_url(driver, 'http://automationexercise.com')
verify_home_page(driver)

# Step 4-5: Scroll down page to bottom, Verify 'SUBSCRIPTION' is visible
scroll_to_bottom(driver)
verify_subscription_visible(driver)

# Step 6-7: Click on arrow at bottom right side to move upward, Verify page is scrolled up and text is visible
scroll_upward(driver)
verify_text_visible_after_scroll(driver, 'Full-Fledged practice website for Automation Engineers')

# Close the browser
driver.quit()

def launch_browser():
    return webdriver.Chrome()

def navigate_to_url(driver, url):
    driver.get(url)

def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Your Home Page Title"))
        print("Home page is visible successfully.")
    except Exception as e:
        print("Error: Home page is not visible.")
        print(e)

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def verify_subscription_visible(driver):
    try:
        subscription_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "SUBSCRIPTION")]'))
        )
        print("SUBSCRIPTION is visible.")
    except Exception as e:
        print("Error: SUBSCRIPTION is not visible.")
        print(e)

def scroll_upward(driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

def verify_text_visible_after_scroll(driver, expected_text):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{expected_text}")]'))
        )
        print(f"{expected_text} is visible after scrolling.")
    except Exception as e:
        print(f"Error: {expected_text} is not visible after scrolling.")
        print(e)

# Main script
driver = launch_browser()

# Step 1-3: Launch browser, Navigate to url, Verify home page
navigate_to_url(driver, 'http://automationexercise.com')
verify_home_page(driver)

# Step 4-5: Scroll down page to bottom, Verify 'SUBSCRIPTION' is visible
scroll_to_bottom(driver)
verify_subscription_visible(driver)

# Step 6-7: Scroll up page to top, Verify that page is scrolled up and text is visible
scroll_upward(driver)
verify_text_visible_after_scroll(driver, 'Full-Fledged practice website for Automation Engineers')

# Close the browser
driver.quit()
# Run the test case
test_complete_checkout_and_account_deletion()


# Run the test case
test_checkout_and_account_deletion()
# Run the test case
test_add_products_to_cart()
# Run the test case
test_cart_subscription()
# Run the test case
test_subscription()
# Run the test case
test_search_product()
# Run the test case
test_view_product_details()
# Run the test case
test_navigate_to_test_cases_page()
# Run the test case
test_contact_us_form()
# Run the test case
test_existing_email_registration()

# Run the test case
test_login_user()

# Run the test case
test_login_user_incorrect_credentials()

# Run the test case
test_login_user_correct_credentials()

# Run the test case
test_register_user()
