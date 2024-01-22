import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    # Replace with your email and password (use an app password if using Gmail)
    email_address = "wkipchumba.wk15@gmail.com"
    email_password = "dbzj crid hkdl aqcg"

    # Replace with the recipient's email address
    recipient_email = "wkipchumba.wk15@gmail.com"

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (replace smtp.gmail.com and 587 with your provider's details)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, recipient_email, message.as_string())



# Example API Test
url = "https://restful-booker.herokuapp.com/example"
headers = {"Content-Type": "application/json"}
data = {"key": "value"}

response = requests.post(url, headers=headers, json=data)

try:
    response.raise_for_status()
    print("Example API Test Passed.")
except requests.exceptions.HTTPError as err:
    print(f"Example API Test Failed. Status Code: {response.status_code}")
    print(f"Error Details: {err}")
    # You can choose to raise the exception or handle it based on the specific use case.




url = "https://restful-booker.herokuapp.com/auth"
headers = {"Content-Type": "application/json"}
data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, headers=headers, json=data)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
print("Token created successfully.")


url = "https://restful-booker.herokuapp.com/booking"

response = requests.get(url)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
print("Booking IDs retrieved successfully.")


booking_id = 1
url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

response = requests.get(url)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
print("Booking details retrieved successfully.")


url = "https://restful-booker.herokuapp.com/booking"
headers = {"Content-Type": "application/json"}
data = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

response = requests.post(url, headers=headers, json=data)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
print("Booking created successfully.")




# Update Booking
booking_id = 1
url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": "token=abc123"
}
data = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

response = requests.put(url, headers=headers, json=data)

try:
    response.raise_for_status()
    print("Booking updated successfully.")
except requests.exceptions.HTTPError as err:
    print(f"Failed to update booking. Status Code: {response.status_code}")
    print(f"Error Details: {err}")
    print(f"Response Content: {response.content.decode('utf-8')}")



booking_id = 1
url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
headers = {
    "Content-Type": "application/json",
    "Cookie": "token=abc123"
}

response = requests.delete(url, headers=headers)
assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
print("Booking deleted successfully.")


url = "https://restful-booker.herokuapp.com/ping"

response = requests.get(url)
assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
print("API health check passed.")



# Test Case: Get Booking IDs with Filters (Booking - GetBookingIds)
# Scenario: Retrieve booking IDs with specific filters.
url = "https://restful-booker.herokuapp.com/booking"
params = {
    "firstname": "Jim",
    "lastname": "Brown",
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
}

response = requests.get(url, params=params)
assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
print("Filtered Booking IDs retrieved successfully.")

# Test Case: Get Booking with Invalid ID (Booking - GetBooking)
# Scenario: Attempt to retrieve a booking with an invalid ID.
invalid_booking_id = 9999
url = f"https://restful-booker.herokuapp.com/booking/{invalid_booking_id}"

response = requests.get(url)
assert response.status_code == 404, f"Unexpected status code: {response.status_code}"
print("Invalid Booking ID handling verified.")

# Test Case: Create Booking with Missing Data (Booking - CreateBooking)
# Scenario: Attempt to create a booking with missing required data.
url = "https://restful-booker.herokuapp.com/booking"
headers = {"Content-Type": "application/json"}
data = {
    "firstname": "John",
    "totalprice": 100
}

response = requests.post(url, headers=headers, json=data)
assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
print("Handling missing data during booking creation verified.")

# Test Case: Update Booking with Invalid ID (Booking - UpdateBooking)
# Scenario: Attempt to update a booking with an invalid ID.
invalid_booking_id = 9999
url = f"https://restful-booker.herokuapp.com/booking/{invalid_booking_id}"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": "token=abc123"
}
data = {
    "firstname": "UpdatedName"
}

response = requests.put(url, headers=headers, json=data)
assert response.status_code == 404, f"Unexpected status code: {response.status_code}"
print("Invalid Booking ID handling during update verified.")


# Email results for Frontend Tests
frontend_results = "Frontend Test Results:\nTest 1: Passed\nTest 2: Failed"
frontend_subject = "CANDIDATE NAME+Frontend test results"
send_email(frontend_subject, frontend_results)
print("Frontend test results emailed successfully.")
