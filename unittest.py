import unittest
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Import your test cases
from testcase1 import test_register_user
from testcase2 import test_login_and_delete_account
from testcase3 import test_login_with_incorrect_credentials
from testcase4 import test_login_and_logout
from testcase5 import test_existing_user_signup
from testcase7 import test_navigate_to_test_cases
from testcase10 import test_subscribe_newsletter
from testcase11 import test_subscribe_newsletter

# List of test functions
test_functions = [
    test_register_user,
    test_login_and_delete_account,
    test_login_with_incorrect_credentials,
    test_login_and_logout,
    test_existing_user_signup,
    test_navigate_to_test_cases,
    test_subscribe_newsletter
    # Add more test functions as needed
]

# Function to run a single test function
def run_test(test_function):
    try:
        test_function()
        return f"{test_function.__name__}: Passed"
    except Exception as e:
        return f"{test_function.__name__}: Failed. Reason: {str(e)}"

# Function to run all test functions in parallel
def run_all_tests():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(run_test, test_functions))

    # Count passed and failed test cases
    passed_count = results.count('Passed')
    failed_count = results.count('Failed')

    # Send email with test results
    send_email('Test Results', '\n'.join(results))

    # Email results for Frontend Tests
    frontend_results = f"Frontend Test Results:\n- Passed: {passed_count}\n- Failed: {failed_count}"
    frontend_subject = "Willy barmasai + Frontend test results"
    send_email(frontend_subject, frontend_results)
    print("Frontend test results emailed successfully.")

# Function to send email with test results
def send_email(subject, body):
    sender_email = 'wkipchumba.wk15@gmail.com'
    sender_password = 'dbzj crid hkdl aqcg'
    receiver_email = 'nbv.service.desk@gmail.com'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    try:
        # Set up the browser once for all tests
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        browser = webdriver.Chrome(options=chrome_options)

        # Run all tests in parallel
        run_all_tests()
    finally:
        # Quit the browser after all tests are done
        browser.quit()
