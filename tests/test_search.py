import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.SearchPage import Search
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch(logclass):
    def test_search_for_a_valid_product(self):
        log = self.getthelogs()
        search_data = Search(self.driver)
        log.info('TEST CASE, test_search_for_a_valid_product')
        log.info("Test Case Starting")
        search_data.input_search(config.get("search","search_hp"))
        search_data.click_on_search_button()
        time.sleep(2)
        if search_data.display_data():
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
        
    def test_search_for_a_invalid_product(self):
        log = self.getthelogs()
        search_data = Search(self.driver)
        log.info('TEST CASE, test_search_for_a_invalid_product')
        log.info("Test Case Starting")
        search_data.input_search(config.get("search","search_honda"))
        search_data.click_on_search_button()
        time.sleep(2)
        expected_text = config.get("expected","expected_text")
        if search_data.invalid_result().__eq__(expected_text):
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
        
    def test_search_without_providing_any_product(self):
        log = self.getthelogs()
        search_data = Search(self.driver)
        log.info('TEST CASE, test_search_without_providing_any_product')
        log.info("Test Case Starting")
        search_data.input_search('')
        search_data.click_on_search_button()
        time.sleep(2)
        expected_text = config.get("expected","expected_text")
        if search_data.invalid_result().__eq__(expected_text):
            assert True
            log.info("Test Case Pass")
        else:
            log.critical("Test Case Fail")
            assert False
  