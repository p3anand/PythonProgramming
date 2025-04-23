# FIXTURES
# gives context to the test.
# Similar to - pre-condition, post-condition.

import pytest


@pytest.fixture()
def is_married():
    return True

#whatever is_married function return its passed as parameter
# in the below function
def test_i_need_confirm(is_married):
    assert is_married == False


@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

@pytest.fixture()
def read_json_file():
    return "{}"


def test_consume(create_token,create_booking_id,read_json_file,read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_json_file)
    print(read_excel_file)