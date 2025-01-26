import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():    
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def driver_offline_setup():
    serv_obj = Service("C:\Drivers\chromedriver-win32\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver