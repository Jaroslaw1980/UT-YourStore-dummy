import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Selenium.UTYourStore.pages.registerAccount import RegisterAccount
from Selenium.UTYourStore.Utilities.utilities import TestUtilities


class RegisterAccountTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path='C:/Selenium - dev/Drivers/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('http://tutorialsninja.com/demo/index.php?route=account/register')
        cls.logger = TestUtilities.logger()
        cls.register = RegisterAccount(cls.driver)
        
    @classmethod
    def tearDownClass(cls):
        clear_browser_data = TestUtilities(cls.driver)
        clear_browser_data.clear_browser_data()
        cls.driver.close()
        cls.driver.quit()

    def test_firstname_input(self):

        log = RegisterAccountTest.logger
        self.firstname = 'Y'

        RegisterAccountTest.register.input_firstname(self.firstname)
        log.info(f'Inputed firstname: {self.firstname}')
        assert 1 < (len(self.firstname)) < 32, log.info('First Name must be between 1 and 32 characters!')

    def test_lastname_input(self):

        log = RegisterAccountTest.logger
        self.lastname = 'B'

        RegisterAccountTest.register.input_lastname(self.lastname)
        log.info(f'Inputed lastname: {self.lastname}')
        assert 1 < (len(self.lastname)) < 32, log.info('Last Name must be between 1 and 32 characters!')

    def test_email_input(self):

        log = RegisterAccountTest.logger
        self.email = 'YaroBarogmail.com'

        RegisterAccountTest.register.input_email(self.email)
        log.info(f'Inputed email: {self.email}')
        assert self.email != log.info('E-Mail Address does not appear to be valid!')

    def test_telephone_input(self):

        log = RegisterAccountTest.logger
        self.telephone = '666'

        RegisterAccountTest.register.input_telephone(self.telephone)
        log.info(f'Inputed telephone: {self.telephone}')
        assert 3 < (len(self.telephone)) < 32, log.info('Telephone must be between 3 and 32 characters!')

    def test_passwordconfirm_input(self):

        log = RegisterAccountTest.logger
        self.password = 'pas'

        RegisterAccountTest.register.input_password(self.password)
        log.info(f'Inputed password: {self.password}')
        assert 4 < (len(self.password)) < 20, log.info('Password must be between 4 and 20 characters!')

    def test_password_input(self):

        log = RegisterAccountTest.logger
        self.confirm_password = 'password'

        RegisterAccountTest.register.confirm_password(self.confirm_password)
        log.info(f'Confirmed password:  {self.confirm_password}')
        
           
if __name__ == '__main__':
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:/Python/Selenium/UTYourStore/Reports'))

