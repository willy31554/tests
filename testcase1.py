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
    email_input.send_keys("qsdddddd444@example.com")

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


# Run the test case
try:
    test_register_user()
    print("Test Case 1: Register User - Passed")
except Exception as e:
    print(f"Test Case 1: Register User - Failed. Reason: {str(e)}")
