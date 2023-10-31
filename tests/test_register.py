import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.RegisterPage import Register
from Utilities.generate_email import generate_email_time_stamp
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister(logclass):
    def test_create_account_with_mandatory_fields(self):
        log = self.getthelogs()
        register = Register(self.driver)
        log.info('TEST CASE, test_create_account_with_mandatory_fields')
        log.info("Test Case Starting")
        register.click_on_my_account_text()
        register.register_new_user()
        register.input_first_name(config.get("registration","first_name"))
        register.input_last_name(config.get("registration","last_name"))
        register.input_email(generate_email_time_stamp())
        register.input_telephone(config.get("registration","telephone"))
        register.input_password(config.get("registration","password"))
        register.input_confirm_password(config.get("registration","confirm_password"))
        register.checked_agreed_input()
        time.sleep(10)
        register.registeration_form_submit_button()
        time.sleep(10)
        if register.successfully_submitted_data():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
            
    def test_create_account_by_providing_all_fields(self):
        log = self.getthelogs()
        register = Register(self.driver)
        log.info('TEST CASE, test_create_account_by_providing_all_fields')
        log.info("Test Case Starting")
        register.click_on_my_account_text()
        register.register_new_user()
        register.input_first_name(config.get("registration","first_name"))
        register.input_last_name(config.get("registration","last_name"))
        register.input_email(generate_email_time_stamp())
        register.input_telephone(config.get("registration","telephone"))
        register.input_password(config.get("registration","password"))
        register.input_confirm_password(config.get("registration","confirm_password"))
        register.click_on_no_checkbox()
        register.checked_agreed_input()
        time.sleep(10)
        register.registeration_form_submit_button()
        time.sleep(10)
        if register.successfully_submitted_data():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Pass")
            assert False
