from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Register:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_link_text_my_account_xpath = "//span[text()='My Account']"
        self.new_user_registeration_xpath = 'Register'
        self.fill_firstname_input_xpath = 'input-firstname'
        self.fill_lastname_input_xpath = 'input-lastname'
        self.fill_email_input_xpath = 'input-email'
        self.fill_telephone_input_xpath = 'input-telephone'
        self.fill_password_input_xpath = 'input-password'
        self.confirm_password_xpath = 'input-confirm'
        self.checked_agreed_xpath = 'agree'
        self.click_submt_on_registeration_xpath = '//input[@value="Continue"]'
        self.successfully_content_show_xpath = 'content'
        self.click_on_no_checkbox_xpath = '//input[@value="1"][@name="newsletter"]'
        self.invalid_message_xpath = 'div.text-danger'
        self.display_invalid_message_xpath = '//*[@id="content"]/form/fieldset[2]/div[2]/div/div'
        
    def click_on_my_account_text(self):
        self.driver.find_element(By.XPATH,self.click_on_link_text_my_account_xpath).click()
        
    def register_new_user(self):
        self.driver.find_element(By.LINK_TEXT,self.new_user_registeration_xpath).click()
        
    def input_first_name(self, firstname):
        self.driver.find_element(By.ID,self.fill_firstname_input_xpath).send_keys(firstname)
        
    def input_last_name(self, lastname):
        self.driver.find_element(By.ID,self.fill_lastname_input_xpath).send_keys(lastname)
        
    def input_email(self, email):
        self.driver.find_element(By.ID,self.fill_email_input_xpath).send_keys(email)
        
    def input_telephone(self, telephone):
        self.driver.find_element(By.ID,self.fill_telephone_input_xpath).send_keys(telephone)
        
    def input_password(self, password):
        self.driver.find_element(By.ID,self.fill_password_input_xpath).send_keys(password)
        
    def input_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID,self.confirm_password_xpath).send_keys(confirm_password)
        
    def checked_agreed_input(self):
        self.driver.find_element(By.NAME,self.checked_agreed_xpath).click()
        
    def registeration_form_submit_button(self):
        self.driver.find_element(By.XPATH,self.click_submt_on_registeration_xpath).click()
        
    def successfully_submitted_data(self):
        return self.driver.find_element(By.ID,self.successfully_content_show_xpath).is_displayed()
    
    def click_on_no_checkbox(self):
        self.driver.find_element(By.XPATH,self.click_on_no_checkbox_xpath).click()
        
    def display_validation_message(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.invalid_message_xpath).is_displayed()
    
    def display_invalid_message(self):
        return self.driver.find_element(By.XPATH,self.display_invalid_message_xpath).text
