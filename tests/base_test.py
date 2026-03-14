import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/index.php")
        self.home_page = HomePage(self.driver)

    def TearDown(self):
        self.driver.quit()