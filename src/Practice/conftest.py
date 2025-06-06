#You don’t have to import Conftest. Python will automatically import it.
#ALl the test cases in the package can use this Conftest
#You cannot change the file name

import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    #we are getting username & password from .env file
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    print("Creating Token....")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    print("Create Booking ID!!")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


@pytest.fixture
def read_csv_file_data():
    pass


@pytest.fixture
def read_mysql_file_database():
    pass


@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"


@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "closed"


@pytest.fixture
def read_url_testdata_excel():
    pass