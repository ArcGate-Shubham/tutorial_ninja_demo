import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.EditProfile import EditProfile
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestEditProfile(logclass):
    def test_edit_profile_with_valid_credientials(self):
        log = self.getthelogs()
        login = Login(self.driver)
        edit_profile = EditProfile(self.driver)
        log.info('TEST CASE, test_edit_profile_with_valid_credientials')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        time.sleep(3)
        login.click_on_login_link_text()
        time.sleep(3)
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        time.sleep(3)
        login.click_on_edit_our_profile_information()
        time.sleep(5)
        edit_profile.update_input_firstname(config.get("registration","updated_first_name"))
        edit_profile.update_input_lastname(config.get("registration","updated_last_name"))
        edit_profile.update_email(config.get("crediential","login_email"))
        edit_profile.update_phone(config.get("registration","updated_telephone"))
        time.sleep(5)
        edit_profile.click_on_submit_button()
        time.sleep(5)
        if edit_profile.display_successfully_updated_message():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
