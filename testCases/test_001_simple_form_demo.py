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
        self.driver.close()

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
        self.driver.close()
        
        
        
        
        