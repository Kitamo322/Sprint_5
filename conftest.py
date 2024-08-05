import pytest
from data import Data
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.StellarBurger_Main_URL)
    chrome_driver.set_window_size(1920, 1080)
    yield chrome_driver
    chrome_driver.quit()
