from pages.home_page import HomePage
from tests.base_test import BaseTest
from time import sleep
from test_data.registration_data import RegistrationDataGenerator
from ddt import ddt, data, unpack
import test_data.registration_data

@ddt
class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account_btn()

    @data(*test_data.registration_data.get_csv_data("test_data/registration.csv"))
    @unpack
    def testNoLastname(self, gender, firstname, lastname, email, password, day, month, year):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(firstname)
        # print(self.create_account_page.get_entered_email())
        # print(self.data.EMAIL)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())
        self.create_account_page.enter_password(self.data.password)
        self.create_account_page.select_date_of_birth(self.data.DATE_OF_BIRTH)
        self.create_account_page.click_register_button()
        expected_number_of_errors = "There is 1 error"
        actual_number_of_errors = self.create_account_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors, actual_number_of_errors)
        visible_errors = (self.create_account_page.get_visible_errors())
        expected_errors = ['lastname is required.']
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(3)

    def testNoPassword(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        self.create_account_page.enter_last_name(self.data.LAST_NAME)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())
        self.create_account_page.select_date_of_birth(self.data.DATE_OF_BIRTH)
        self.create_account_page.click_register_button()
        expected_number_of_errors = "There is 1 error"
        actual_number_of_errors = self.create_account_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors, actual_number_of_errors)
        visible_errors = (self.create_account_page.get_visible_errors())
        expected_errors = ['passwd is required.']
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(3)

    def testNoFirstName(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_last_name(self.data.LAST_NAME)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.select_date_of_birth(self.data.DATE_OF_BIRTH)
        self.create_account_page.click_register_button()
        expected_number_of_errors = "There is 1 error"
        actual_number_of_errors = self.create_account_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors, actual_number_of_errors)
        visible_errors = (self.create_account_page.get_visible_errors())
        expected_errors = ['firstname is required.']
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(3)