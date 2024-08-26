import time

from seleniumpagefactory.Pagefactory import PageFactory
from tests.utils.commom_utils import webdriver_wait_url


class DashboardPage(PageFactory):  # TODO - 1.Single Inheritance
    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True

    locators = {
        'username_logged_in': ('XPATH', "//span[@data-qa='lufexuloga']")
    }

    def user_logged_in_text(self):
        webdriver_wait_url(driver=self.driver, timeout=10)
        return self.username_logged_in.get_text()
