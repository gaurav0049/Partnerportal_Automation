import time


import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class Test_Pomangment:
    def test_button(self):
        self.driver.find_element(By.XPATH,"//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()






