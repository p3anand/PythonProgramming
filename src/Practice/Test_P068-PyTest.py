# PyTest

import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke(reason = "Future") #You can add this to skip execution of this
def test_test_case1():
    print ("Hello TC1")

@pytest.mark.regression
def test_test_case2():
    print ("Hello TC2")

@pytest.mark.skip
def test_test_case3():
    print ("Hello TC3")

def test_verify_sum():
    assert 1 + 1 == 2

def test_verify_sub1():
    assert 1 - 1 == 2

def test_verify_sub2():
    assert 2 - 1 == 2

def test_verify_sub3():
    assert 4 - 2 == 2