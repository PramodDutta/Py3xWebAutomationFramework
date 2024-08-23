import time

import allure
import pytest
from selenium import webdriver
from tests.pageObejcts.pom.loginPage import LoginPage
from tests.pageObejcts.pom.dashboardPage import DashboardPage
from tests.utils.commom_utils import webdriver_wait
from tests.constants.constants import Constants


# Assertions and use the Page Object class

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(usr="contact+atb7x@thetestingacademy.com", pwd="Wingify@1235")
    time.sleep(2)
    error_msg_element = login_page.get_error_message_text()
    assert error_msg_element == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(usr="pyatb3x@wingify.com", pwd="Wingify@1234")
    dashboardPage = DashboardPage(driver=setup)
    assert "Aman Ji" in dashboardPage.user_logged_in_text()
