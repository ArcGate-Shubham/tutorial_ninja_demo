import time
import pytest
import configparser
from PageObjects.LoginPage import Login
from PageObjects.ModifyAddressBookPage import ModifyAddressBook
from Utilities.logger import logclass
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestModifyAddress(logclass):
    def test_modify_address_book_with_valid_data(self):
        log = self.getthelogs()
        
        login = Login(self.driver)
        log.info('TEST CASE, test_modify_address_book_with_valid_data')
        log.info("Test Case Starting")
        login.click_on_my_account_link_text()
        login.click_on_login_link_text()
        login.input_email(config.get("crediential","login_email"))
        login.input_password(config.get("crediential","login_password"))
        login.click_on_submit_button()
        for click_data in login.click_modify_address_word():
            if 'Modify your address book entries' in click_data.get_attribute('innerHTML'):
                click_data.click()
                break
            
        modifyaddress = ModifyAddressBook(self.driver)
        for add_new_address in modifyaddress.click_new_address_button():
            if 'New Address' in add_new_address.get_attribute('innerHTML'):
                add_new_address.click()
                break
        modifyaddress.input_first_name('data')
        modifyaddress.input_last_name('data')
        modifyaddress.input_company_name('data')
        modifyaddress.input_address_one('data')
        modifyaddress.input_address_two('data')
        modifyaddress.input_city('data')
        modifyaddress.input_postcode('305001')
        modifyaddress.input_country('India')
        time.sleep(1)
        modifyaddress.input_state('Rajasthan')
        modifyaddress.click_on_submit_button()
        
        if 'Your address has been successfully added' in modifyaddress.display_successfully_message().text:
            assert True
            log.info("Test Case Pass")
        else:
            log.info("Test Case Fail")
            self.driver.save_screenshot('Screenshots/test_modify_address_book_with_valid_data.png')
            assert False
