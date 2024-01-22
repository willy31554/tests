from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_contact_us():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1-3: Launch browser, Navigate to url 'http://automationexercise.com', Verify that home page is visible successfully
        driver.get("http://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("Step 1-3: Successfully opened the website - Pass")

        # Step 4-5: Click on 'Contact Us' button, Verify 'GET IN TOUCH' is visible
        contact_us_button = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a")
        contact_us_button.click()

        # Wait for the 'GET IN TOUCH' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='GET IN TOUCH']")))

        assert "GET IN TOUCH" in driver.page_source
        print("Step 4-5: Clicked on 'Contact Us' button and verified 'GET IN TOUCH' is visible - Pass")


        # Step 6-7: Enter name, email, subject, and message
        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.NAME, "email")
        subject_input = driver.find_element(By.NAME, "subject")
        message_input = driver.find_element(By.NAME, "message")

        name_input.send_keys("Your Name")
        email_input.send_keys("your_email@example.com")
        subject_input.send_keys("Test Subject")
        message_input.send_keys("Test Message")

        # Step 8: Upload file (Assuming file input has the name "file")
        file_input = driver.find_element(By.NAME, "file")
        file_input.send_keys("path_to_your_file.txt")  # Update with the actual file path

        # Click 'Submit' button
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        submit_button.click()

        print("Step 6-8: Entered details, Uploaded file, and Clicked 'Submit' button - Pass")

        # Step 9: Click OK button (assuming it's an alert)
        alert = driver.switch_to.alert
        alert.accept()
        print("Step 9: Clicked OK on the alert - Pass")

        # Step 10: Verify success message 'Success! Your details have been submitted successfully.' is visible
        success_message_xpath = "//div[contains(text(), 'Success! Your details have been submitted successfully.')]"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, success_message_xpath))
        )
        assert "Success! Your details have been submitted successfully." in driver.page_source
        print("Step 10: Verified success message is visible - Pass")

        # Step 11: Click 'Home' button and verify that landed to the home page successfully
        home_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Home')]")
        home_button.click()

        # Wait for the 'Automation Exercise' element to be present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Automation Exercise']")))

        assert "Automation Exercise" in driver.page_source
        print("Step 11: Clicked 'Home' button and verified landing on the home page - Pass")

    except Exception as e:
        print(f"Test Case: Contact Us - Failed. Reason: {str(e)}")

    finally:
        driver.quit()

# Run the test case
try:
    test_contact_us()
    print("Test Case: Contact Us - Passed")
except Exception as e:
    print(f"Test Case: Contact Us - Failed. Reason: {str(e)}")
