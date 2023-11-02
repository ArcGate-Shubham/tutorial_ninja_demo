import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(logclass):    
    def test_login_with_valid_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_valid_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_edit_your_account_information():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False

        
    def test_login_without_entering_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_without_entering_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email('')
        login.input_password('')
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_login_with_incorrect_email_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_incorrect_email_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_incorrect_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_login_with_incorrect_password_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_incorrect_password_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_incorrect_password"))
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False

    def test_login_with_correct_email_blank_password_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_correct_email_blank_password_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_email"))
        login.input_password('')
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_login_with_blank__email_correct_password_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_blank__email_correct_password_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email('')
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_login_with_incorrect_email_blank_password_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_incorrect_email_blank_password_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_incorrect_email"))
        login.input_password('')
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_login_with_blank_email_incorrect_password_credentials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_login_with_blank_email_incorrect_password_credentials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email('')
        login.input_password(config.get("crediential","login_incorrect_password"))
        login.click_on_submit_button()
        time.sleep(3)
        if login.display_invalid_credientials_data():
            assert True
            time.sleep(3)
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
