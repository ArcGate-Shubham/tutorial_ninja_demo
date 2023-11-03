import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChangePassword:
    def __init__(self, driver):
        self.driver = driver
        self.change_password_input_xpath = 'input-password'
        self.change_confirm_password_input_xpath = 'input-confirm'
        self.click_on_continued_button_xpath = '//input[@value="Continue"]'
        self.success_messege_display_xpath = 'div.alert-success'
        self.invalid_message_display_xpath = 'div.text-danger'
        self.invalid_message_for_confirm_password_input_xpath = '//*[@id="content"]/form/fieldset/div[2]/div/div'
    
    def update_input_password(self, password):
        wait = WebDriverWait(self.driver, 5)
        change_password = wait.until(EC.presence_of_element_located((By.ID, self.change_password_input_xpath)))
        change_password.send_keys(password)
        
    def update_input_confirm_password(self, confirm_password):
        wait = WebDriverWait(self.driver, 5)
        change_confirm_password = wait.until(EC.presence_of_element_located((By.ID, self.change_confirm_password_input_xpath)))
        change_confirm_password.send_keys(confirm_password)
        
    def clicked_on_continued_button(self):
        wait = WebDriverWait(self.driver, 5)
        continued_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_continued_button_xpath)))
        continued_button.click()
        
    def display_success_message(self):
        wait = WebDriverWait(self.driver, 5)
        display_success_message_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.success_messege_display_xpath)))
        return display_success_message_data.is_displayed()
    
    def display_error_message(self):
        wait = WebDriverWait(self.driver, 5)
        display_error_message_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.invalid_message_display_xpath)))
        return display_error_message_data.is_displayed()
    
    def display_both_validation_error(self):
        wait = WebDriverWait(self.driver, 5)
        display_error_message_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.invalid_message_display_xpath)))
        display_error_message_data_value = wait.until(EC.presence_of_element_located((By.XPATH, self.invalid_message_for_confirm_password_input_xpath)))
        return display_error_message_data.is_displayed() and display_error_message_data_value.is_displayed()
