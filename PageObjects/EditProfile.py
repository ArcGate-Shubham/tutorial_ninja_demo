import time
from selenium.webdriver.common.by import By


class EditProfile:
    def __init__(self, driver):
        self.driver = driver
        self.update_input_firstname_xpath = 'input-firstname'
        self.update_input_lastname_xpath = 'input-lastname'
        self.update_email_xpath = 'input-email'
        self.update_phone_xpath = 'input-telephone'
        self.click_on_submit_button_xpath = 'input.btn.btn-primary'
        self.display_successfully_updated_message_xpath = 'div.alert-success'
        
    def update_input_firstname(self, firstname):
        update_firstname = self.driver.find_element(By.ID,self.update_input_firstname_xpath)
        update_firstname.clear()
        time.sleep(3)
        update_firstname.send_keys(firstname)
        
    def update_input_lastname(self, lastname):
        update_lastname = self.driver.find_element(By.ID,self.update_input_lastname_xpath)
        update_lastname.clear()
        time.sleep(3)
        update_lastname.send_keys(lastname)
        
    def update_email(self, email):
        update_email = self.driver.find_element(By.ID,self.update_email_xpath)
        update_email.clear()
        time.sleep(3)
        update_email.send_keys(email)
        
    def update_phone(self, telephone):
        update_phone = self.driver.find_element(By.ID,self.update_phone_xpath)
        update_phone.clear()
        time.sleep(3)
        update_phone.send_keys(telephone)
        
    def click_on_submit_button(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR,self.click_on_submit_button_xpath)
        submit_button.click()
        
    def display_successfully_updated_message(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.display_successfully_updated_message_xpath).is_displayed()
