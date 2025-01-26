from selenium.webdriver.common.by import By

class HomePage():
    lnk_simple_form_xpath = "//a[normalize-space()='Simple Form Demo']"
    lnk_simple_form_input_message = "//input[@id='user-message']"
    lnk_get_checked_value = "//button[@id='showInput']"
    lnk_your_message = "//p[@id='message']"
    lnk_drag_drop_sliders = "//a[normalize-space()='Drag & Drop Sliders']"
    lnk_default_value_15_slider = "//input[@value='15']"
    lnk_input_form_submit = "//a[normalize-space()='Input Form Submit']"
    lnk_submit_form = "//button[normalize-space()='Submit']"

    def __init__(self, driver):
        self.driver = driver
    
    def clickSimpleFormDemo(self):
        self.driver.find_element(By.XPATH, self.lnk_simple_form_xpath).click()
    
    def input_message_box(self):
        item = self.driver.find_element(By.XPATH, self.lnk_simple_form_input_message)

    def click_get_checked_value(self):
        self.driver.find_element(By.XPATH, self.lnk_get_checked_value).click()
    
    def your_message(self):
        msg = self.driver.find_element(By.XPATH, self.lnk_your_message)
        return msg
    
    def click_drag_drop_sliders(self):
        self.driver.find_element(By.XPATH,self.lnk_drag_drop_sliders).click()

    def get_default_value_15_slider(self):
        return self.driver.find_element(By.XPATH, self.lnk_default_value_15_slider)
    
    def lnk_input_form_submit(self):
        self.driver.find_element(By.XPATH, self.lnk_input_form_submit).click()
    
    def submit_form(self):
        self.driver.find_element(By.XPATH, self.lnk_submit_form).click()

