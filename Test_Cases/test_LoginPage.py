import configparser
import time
import unittest

from selenium import webdriver

from Selenium_Python_POM_UnitTest.Page_Objects.LoginPage import LoginToGithub
from Selenium_Python_POM_UnitTest.Page_Objects.RegistrationPage import Registration

config = configparser.ConfigParser()
config.read('/Users/rakjha/PyProjects/POM_UnitTest_Project/config.ini')


class Github_Login_Functionality_validation(unittest.TestCase):
    def setUp(self):
        self.baseURL = str(config['git_url']['url'])
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        self.rp = Registration(self.driver)
        self.lp = LoginToGithub(self.driver)

    """
    Test case 1 : Registration test case to Github.
    Use valid user name, email and password to test the test case to register to github.
    parameter1 : is user name
    parameter2 : is email
    parameter3 : is password
    """

    def test_Registration(self):
        self.driver.get(self.baseURL)
        parameter1 = str(config['sign_up']['email'])
        parameter2 = str(config['sign_up']['password'])
        parameter3 = str(config['sign_up']['retypePassword'])
        self.rp.UserRegistration(parameter1, parameter2, parameter3)
        result = self.rp.VerifyRegistration()
        self.assertEqual(result, True)

    """
    Test case 2 : Login test to Github with valid credentials.
    Due to security reasons, user name and password are not provided in the script.
    Use valid user name and password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """

    def test_Login_with_valid_credentials(self):
        self.driver.get(self.baseURL)
        parameter1 = str(config['sign_in']['email'])
        parameter2 = str(config['sign_in']['password'])
        self.lp.UserLogin(parameter1, parameter2)
        time.sleep(5)
        result = self.lp.VerifyLogin()
        self.assertEqual(result, False)

    """
    Test case 3 : Login test to Github with Invalid User name.
    Use Invalid user name and and valid password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """

    def test_Login_with_Invalid_UserName(self):
        self.driver.get(self.baseURL)
        parameter1 = str(config['sign_in']['invalid_email'])
        parameter2 = str(config['sign_in']['password'])
        self.lp.UserLogin(parameter1, parameter2)
        time.sleep(5)
        result = self.lp.VerifyLogin()
        self.assertEqual(result, True)

    """
    Test case 4 : Login test to Github with valid user name and Invalid password.
    Use valid user name and Invalid password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """

    def test_Login_with_Invalid_Password(self):
        self.driver.get(self.baseURL)
        parameter1 = str(config['sign_in']['email'])
        parameter2 = str(config['sign_in']['invalid_password'])
        self.lp.UserLogin(parameter1, parameter2)
        time.sleep(5)
        result = self.lp.VerifyLogin()
        self.assertEqual(result, True)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
