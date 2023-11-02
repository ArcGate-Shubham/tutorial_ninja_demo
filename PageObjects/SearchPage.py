from selenium.webdriver.common.by import By


class Search:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_xpath = 'search'
        self.search_button_xpath = 'btn-default'
        self.display_data_xpath = 'HP LP3065'
        self.display_data_invalid_xpath = '//*[@id="content"]/p[2]'
    
    def input_search(self,Value):
        self.driver.find_element(By.NAME, self.search_input_xpath).send_keys(Value)
        
    def click_on_search_button(self):
        self.driver.find_element(By.CLASS_NAME,self.search_button_xpath).click()
        
    def display_data(self):
        return self.driver.find_element(By.LINK_TEXT,self.display_data_xpath).is_displayed()
    
    def invalid_result(self):
        return self.driver.find_element(By.XPATH,self.display_data_invalid_xpath).text
