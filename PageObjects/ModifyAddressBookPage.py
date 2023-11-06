import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class ModifyAddressBook:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_new_address_xpath = 'div.pull-right'
        self.fill_first_name_value_xpath = 'input-firstname'
        self.fill_last_name_value_xpath = 'input-lastname'
        self.fill_company_name_value_xpath = 'input-company'
        self.fill_address_one_value_xpath = 'input-address-1'
        self.fill_address_two_value_xpath = 'input-address-2'
        self.fill_city_value_xpath = 'input-city'
        self.fill_postal_code_xpath = 'input-postcode'
        self.fill_dropdown_for_country_xpath = 'input-country'
        self.fill_dropdown_for_state_xpath = 'input-zone'
        self.click_continue_button_xpath = '//input[@value="Continue"]'
        self.successfully_registered_xpath = 'div.alert-success'
        
    def click_new_address_button(self):   
        return self.driver.find_elements(By.CSS_SELECTOR,self.click_on_new_address_xpath)
    
    def input_first_name(self, firstname):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fill_first_name_value_xpath)))
        element.send_keys(firstname)
        
    def input_last_name(self, lastname):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fill_last_name_value_xpath)))
        element.send_keys(lastname)
        
    def input_company_name(self, company):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fill_company_name_value_xpath)))
        element.send_keys(company)
        
    def input_address_one(self, address_one):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.fill_address_one_value_xpath)))
        element.send_keys(address_one)
        
    def input_address_two(self, address_two):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, self.fill_address_two_value_xpath)))
        element.send_keys(address_two)
        
    def input_city(self, city):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, self.fill_city_value_xpath)))
        element.send_keys(city)
        
    def input_postcode(self, postcode):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, self.fill_postal_code_xpath)))
        element.send_keys(postcode)
        
    def input_country(self, country):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.fill_dropdown_for_country_xpath)))
        select = Select(select)
        select.select_by_visible_text(country)
        
    def input_state(self, state):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.fill_dropdown_for_state_xpath)))
        select = Select(select)
        select.select_by_visible_text(state)
        
    def click_on_submit_button(self):
        self.driver.find_element(By.XPATH, self.click_continue_button_xpath).click()
        
    def display_successfully_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.successfully_registered_xpath)
