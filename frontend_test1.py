from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_register_user():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-5: Navigate to the website and click on 'Signup / Login'
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title

        #signup_login_button = driver.find_element(By.XPATH, "//button[text()='Signup / Login']")
        signup_login_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        button_text = signup_login_button.text

        signup_login_button.click()

        # Assert the current URL after clicking the signup/login button
        current_url = driver.current_url
        expected_url = "https://automationexercise.com/login"
        assertion_result = current_url == expected_url
        print(f"Assertion Result signUp/login url: {assertion_result}")
        assert assertion_result, f"Expected URL: {expected_url}, Actual URL: {current_url}"

        # Step 6-15: Register user
        assert "New User Signup!" in driver.page_source

        # Fill registration details
        fill_registration_details(driver)

        # Verify 'Logged in as username' is visible
        assert "Logged in as Test User" in driver.page_source

        # Step 16-18: Delete Account
        delete_account_button = driver.find_element(By.XPATH, "//button[text()='Delete Account']")
        delete_account_button.click()

        # Verify 'ACCOUNT DELETED!' is visible
        assert "ACCOUNT DELETED!" in driver.page_source

        # Click 'Continue' button
        continue_button = driver.find_element(By.XPATH, "//button[text()='Continue']")
        continue_button.click()

        # Send email with test results
        send_email('CANDIDATE NAME Frontend test results', 'Register User Test Passed!')
    finally:
        driver.quit()

# def test_login_user_correct_credentials():
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     try:
#         # Step 1-5: Navigate to the website and click on 'Signup / Login'
#         driver.get("http://automationexercise.com")
#         assert "Automation Exercise" in driver.title

#         signup_login_button = driver.find_element(By.XPATH, "//button[text()='Signup / Login']")
#         signup_login_button.click()

#         # Step 6-8: Login with correct email and password
#         assert "Login to your account" in driver.page_source

#         email_input = driver.find_element(By.NAME, "email")
#         password_input = driver.find_element(By.NAME, "password")

#         email_input.send_keys("testuser@example.com")
#         password_input.send_keys("password123")

#         # Click 'Login' button
#         login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
#         login_button.click()

#         # Verify 'Logged in as username' is visible
#         assert "Logged in as Test User" in driver.page_source

#         # Step 9-10: Delete Account
#         delete_account_button = driver.find_element(By.XPATH, "//button[text()='Delete Account']")
#         delete_account_button.click()

#         # Verify 'ACCOUNT DELETED!' is visible
#         assert "ACCOUNT DELETED!" in driver.page_source

#         # Send email with test results
#         send_email('CANDIDATE NAME Frontend test results', 'Login User (Correct Credentials) Test Passed!')
#     finally:
#         driver.quit()

# def test_login_user_incorrect_credentials():
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     try:
#         # Step 1-5: Navigate to the website and click on 'Signup / Login'
#         driver.get("http://automationexercise.com")
#         assert "Automation Exercise" in driver.title

#         signup_login_button = driver.find_element(By.XPATH, "//button[text()='Signup / Login']")
#         signup_login_button.click()

#         # Step 6-8: Login with incorrect email and password
#         assert "Login to your account" in driver.page_source

#         email_input = driver.find_element(By.NAME, "email")
#         password_input = driver.find_element(By.NAME, "password")

#         email_input.send_keys("incorrect@example.com")
#         password_input.send_keys("incorrectpassword")

#         # Click 'Login' button
#         login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
#         login_button.click()

#         # Verify error message is visible
#         assert "Your email or password is incorrect!" in driver.page_source

#         # Send email with test results
#         send_email('CANDIDATE NAME Frontend test results', 'Login User (Incorrect Credentials) Test Passed!')
#     finally:
#         driver.quit()

def fill_registration_details(driver):
    # Fill details: Title, Name, Email, Password, Date of birth
 
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]")
  
 
    name_input.send_keys("Test User")
    email_input.send_keys("testuser@example.com")
  

    #Select checkboxes
    newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
    partner_offers_checkbox = driver.find_element(By.NAME, "partner_offers")

    newsletter_checkbox.click()
    partner_offers_checkbox.click()

    #Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_input = driver.find_element(By.NAME, "firstname")
    last_name_input = driver.find_element(By.NAME, "lastname")
    company_input = driver.find_element(By.NAME, "company")
    address_input = driver.find_element(By.NAME, "address")
    address2_input = driver.find_element(By.NAME, "address2")
    country_input = driver.find_element(By.NAME, "country")
    state_input = driver.find_element(By.NAME, "state")
    city_input = driver.find_element(By.NAME, "city")
    zip_input = driver.find_element(By.NAME, "zip")
    mobile_input = driver.find_element(By.NAME, "mobile")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    company_input.send_keys("XYZ Corp")
    address_input.send_keys("123 Main St")
    address2_input.send_keys("Apt 456")
    country_input.send_keys("United States")
    state_input.send_keys("California")
    city_input.send_keys("Los Angeles")
    zip_input.send_keys("90001")
    mobile_input.send_keys("1234567890")

    # Click 'Create Account' button
    create_account_button = driver.find_element(By.XPATH, "//div[@class='signup-form']//button[contains(text(), 'Signup')]")
    create_account_button.click()

    # Verify that 'ACCOUNT CREATED!' is visible
    assert "ACCOUNT CREATED!" in driver.page_source

    # Click 'Continue' button
    continue_button = driver.find_element(By.XPATH, "//button[text()='Continue']")
    continue_button.click()

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

# Run all three test cases
test_register_user()
test_login_user_correct_credentials()
test_login_user_incorrect_credentials()
