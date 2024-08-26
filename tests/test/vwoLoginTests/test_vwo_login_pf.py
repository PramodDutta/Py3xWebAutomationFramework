import time
import pytest
import selenium
from selenium import webdriver
from tests.pageObejcts.page_factory.loginPage_pf import LoginPage
import allure
from allure_commons.types import AttachmentType
from tests.constants.constants import Constants


@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(Constants.app_url())
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd="123")
        error_msg_element = loginPage.error_msg()
        assert error_msg_element == "Your email, password, IP address or location did not match"

        if "Dashboard" not in driver.title:
            Constants.take_screenshot(driver,"test_vwo_login_negative_tc0")
        time.sleep(10)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc2(self, setup):
        pass

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc3(self, setup):
        pass

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc4(self, setup):
        pass