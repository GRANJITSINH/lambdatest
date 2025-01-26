import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from pageObjects.SimpleFormDemo import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

timeout = 20

class Test_001_SimpleFormDemo:
    baseURL = "https://www.lambdatest.com/selenium-playground"

    def test_health(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.close()
        assert True
        
    def test_simple_form_demo(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.hp = HomePage(self.driver)
        self.hp.clickSimpleFormDemo()
        
        try:
            element_xpath = "//div[normalize-space()='Single Input Field']"
            element_present = EC.presence_of_all_elements_located((By.XPATH, element_xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except:
            print("Timed out waiting fir page to load")
        
        self.get_url = self.driver.current_url
        item = self.hp.input_message_box()
        welcome_msg = "Welcome to LambdaTest"
        item.send_keys(welcome_msg)
        
        self.hp.click_get_checked_value()
        msg = self.hp.your_message().text
        if 'simple-form-demo' in self.get_url and msg == welcome_msg:
            assert True
        else:
            assert False
        self.driver.quit()

class Test_002_DragNDropSliders:
    baseURL = "https://www.lambdatest.com/selenium-playground"
    
    def test_simple_form_demo(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.hp = HomePage(self.driver)
        self.hp.click_drag_drop_sliders()
        
        try:
            element_xpath = "//h4[normalize-space()='Default value 5']"
            element_present = EC.presence_of_all_elements_located((By.XPATH, element_xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except:
            print("Timed out waiting fir page to load")
        
        default_value_15_slider = self.hp.get_default_value_15_slider()
        act = ActionChains(self.driver)
        act.click_and_hold(default_value_15_slider).move_by_offset(120, 0).release().perform()
        target_slider_value = "//output[@id='rangeSuccess']"
        target_slider_75 = self.driver.find_element(By.XPATH, target_slider_value).text
        time.sleep(5)
        
        if target_slider_75 == '75':
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.quit()

class Test_003_InputFormSubmit:
    baseURL = "https://www.lambdatest.com/selenium-playground"
    
    def test_input_form_submit(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.hp = HomePage(self.driver)
        self.hp.input_form_submit()
        self.hp.submit_form()
        ele_name = self.driver.find_element(By.XPATH, "//input[@id='name']")
        validation_message = ele_name.get_attribute("validationMessage")
        print(validation_message)
        try:
            element_xpath = "//input[@id='name']"
            element_present = EC.presence_of_all_elements_located((By.XPATH, element_xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except:
            print("Timed out waiting fir page to load")
            
        # passing data to the application
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys("prince")
        self.driver.find_element(By.XPATH, "//input[@id='inputEmail4']").send_keys("prince@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='inputPassword4']").send_keys("#prince@gmail")
        self.driver.find_element(By.XPATH, "//input[@id='company']").send_keys("lambdatest")
        self.driver.find_element(By.XPATH, "//input[@id='websitename']").send_keys("www.lambdatest.com")
        select = Select(self.driver.find_element(By.XPATH,"//select[@name='country']"))
        select.select_by_visible_text('United States')
        self.driver.find_element(By.XPATH, "//input[@id='inputCity']").send_keys("Newyork")
        self.driver.find_element(By.XPATH, "//input[@id='inputAddress1']").send_keys("Newyork Square")
        self.driver.find_element(By.XPATH, "//input[@id='inputAddress2']").send_keys("Newyork Square-11")
        self.driver.find_element(By.XPATH, "//input[@id='inputState']").send_keys("Newyork")
        self.driver.find_element(By.XPATH, "//input[@id='inputZip']").send_keys("11")
        
        self.hp.submit_form()
        
        try:
            element_xpath = "//p[@class='success-msg hidden']"
            element_present = EC.presence_of_all_elements_located((By.XPATH, element_xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except:
            print("Timed out waiting fir page to load")
        time.sleep(4)
        
        lnk_validate_success_msg = "//p[@class='success-msg hidden']"
        print(lnk_validate_success_msg)
        validate_success_msg = self.driver.find_element(By.XPATH, lnk_validate_success_msg).text
        
        if validation_message == "Please fill out this field." and validate_success_msg == "Thanks for contacting us, we will get back to you shortly.":
            assert True
        else:
            assert False
        
        time.sleep(4)
        self.driver.quit()
        
        
        
    
        
        
        
        
        