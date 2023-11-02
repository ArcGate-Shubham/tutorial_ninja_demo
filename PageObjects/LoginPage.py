from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.click_my_account_link_text_xpath = "//span[text()='My Account']"
        self.click_login_link_text_xpath = 'Login'
        self.fill_input_email_xpath = 'email'
        self.fill_input_password_xpath = 'password'
        self.click_submit_button_xpath = 'input.btn-primary'
        self.display_link_text_xpath = 'Edit your account information'
        self.display_invalid_crediential_xpath = 'div.alert-dismissible'
        
    def click_on_my_account_link_text(self):
        self.driver.find_element(By.XPATH,self.click_my_account_link_text_xpath).click()
        
    def click_on_login_link_text(self):
        self.driver.find_element(By.LINK_TEXT,self.click_login_link_text_xpath).click()
        
    def input_email(self, email):
        self.driver.find_element(By.NAME,self.fill_input_email_xpath).send_keys(email)
        
    def input_password(self,password):
        self.driver.find_element(By.NAME,self.fill_input_password_xpath).send_keys(password)
        
    def click_on_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click_submit_button_xpath).click()
        
    def display_edit_your_account_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.display_link_text_xpath).is_displayed()
    
    def display_invalid_credientials_data(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.display_invalid_crediential_xpath).is_displayed()
    
    def click_on_edit_our_profile_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.display_link_text_xpath).click()
