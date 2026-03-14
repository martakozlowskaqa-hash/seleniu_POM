from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    Create Account Page locators
    """
    FIRST_NAME = (By.ID, 'customer_firstname')

class CreateAccountPage(BasePage):
    """
    Create Account Page Object
    """
    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def _verify_page(self):
        #todo: improve this!!
        sleep(3)
