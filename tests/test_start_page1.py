""" Tests relates to start page """
from time import sleep

from selenium import webdriver


class TestStartPage:
    """Stares tests for start page base functionality"""

    def test_start_page(self):
        driver = webdriver.Chrome(executable_path="/chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        sleep(1)
        driver.close()
