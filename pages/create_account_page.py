import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from time import sleep
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
    REGISTER_BTN = (By.ID, 'submitAccount')
    YEAR_OF_BIRTH = (By.ID, 'years')
    MONTH_OF_BIRTH = (By.ID, 'months')
    DAY_OF_BIRTH = (By.ID, 'days')
    VISIBLE_ERORRS = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
    NUMBER_OF_ERRORS = (By.XPATH, '//div[@class="alert alert-danger"]/p')

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
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.FIRST_NAME))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BTN))

    def select_date_of_birth(self,date_of_birth):
        birth_day = Select(self.driver.find_element(*Locators.DAY_OF_BIRTH))
        birth_day.select_by_value(str(date_of_birth.day))
        month_s = Select(self.driver.find_element(*Locators.MONTH_OF_BIRTH))
        month_s.select_by_value(str(date_of_birth.month))
        year_s = Select(self.driver.find_element(*Locators.YEAR_OF_BIRTH))
        year_s.select_by_value(str(date_of_birth.year))

    def click_register_button(self):
        self.driver.find_element(*Locators.REGISTER_BTN).click()

    def get_number_of_errors_message(self):
        return self.driver.find_element(*Locators.NUMBER_OF_ERRORS).text

    def get_visible_errors(self):
        errors_webelements = self.driver.find_elements(*Locators.VISIBLE_ERORRS)
        visible_errors = []
        for error in errors_webelements:
            visible_errors.append(error.text)
        return visible_errors
