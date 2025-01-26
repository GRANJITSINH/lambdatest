import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

@pytest.fixture()
def driver_offline_setup():
    serv_obj = Service("")
    driver = webdriver.Chrome(service=serv_obj)
    return driver