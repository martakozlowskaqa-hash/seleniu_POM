from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.custom_types import Gender

class Locators:
    """
    Create Account Page locators
    """
    FIRST_NAME = (By.ID, 'customer_firstname')
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')

class CreateAccountPage(BasePage):
    """
    Create Account Page Object
    """
    def choose_gender(self,gender):
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)


    def get_entered_email(self):
        """"
        Assert reapeted email from previous page
        """
        return self.driver.find_element(*Locators.EMAIL).get_attribute("value")

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)


    def _verify_page(self):
        #todo: improve this!!
        sleep(3)
