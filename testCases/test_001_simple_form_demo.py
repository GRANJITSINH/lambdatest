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

    def test_simple_form_demo(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        assert True