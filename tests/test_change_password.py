import time
import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.EditProfile import EditProfile
from PageObjects.ChangePasswordPage import ChangePassword
from Utilities.logger import logclass
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestChangePassword(logclass):
    def test_change_password_with_valid_data(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_change_password_with_valid_data')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        login.click_on_login_link_text()
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        login.click_on_Change_your_password()
        
        change = ChangePassword(self.driver)
        password = change.update_input_password(config.get("registration","changed_password"))
        confirm_password = change.update_input_confirm_password(config.get("registration","changed_confirm_password"))
        if password == confirm_password:
            change.clicked_on_continued_button()
            time.sleep(5)
            if change.display_success_message():
                assert True
                log.info('Test Case Pass')
            else:
                self.driver.save_screenshot('Screenshots/test_change_password_with_valid_data1.png')
                log.critical('Test Case Fail')
                assert False
        else:
            self.driver.save_screenshot('Screenshots/test_change_password_with_valid_data2.png')
            log.critical('Test Case Fail')
            assert False       
        
    def test_change_password_with_invalid_data(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_change_password_with_invalid_data')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        login.click_on_login_link_text()
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        login.click_on_Change_your_password()
        
        change = ChangePassword(self.driver)
        change.update_input_password(config.get("registration","changed_password"))
        change.update_input_confirm_password(config.get("registration","changed_confirm_wrong_password"))
        change.clicked_on_continued_button()
        time.sleep(5)
        if change.display_error_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_change_password_with_invalid_data.png')
            log.critical('Test Case Fail')
            assert False
        
    def test_change_password_without_confirm_password_but_fill_password_input(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_change_password_without_confirm_password_but_fill_password_input')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        login.click_on_login_link_text()
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        login.click_on_Change_your_password()
        
        change = ChangePassword(self.driver)
        change.update_input_password(config.get("registration","changed_password"))
        change.update_input_confirm_password('')
        change.clicked_on_continued_button()
        time.sleep(4)
        if change.display_error_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_change_password_without_confirm_password_but_fill_password_input.png')
            log.critical('Test Case Fail')
            assert False

    def test_change_password_without_password_but_fill_confirm_password_input(self):
        log = self.getthelogs()
        login = Login(self.driver)
        log.info('TEST CASE, test_change_password_without_password_but_fill_confirm_password_input')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        login.click_on_login_link_text()
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        login.click_on_Change_your_password()
        
        change = ChangePassword(self.driver)
        change.update_input_password('')
        change.update_input_confirm_password(config.get("registration","changed_confirm_password"))
        change.clicked_on_continued_button()
        time.sleep(4)
        if change.display_both_validation_error():
            log.info('Test Case Pass')
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_change_password_without_password_but_fill_confirm_password_input.png')
            log.critical('Test Case Fail')
            assert False
