import time

from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class Test_Pomangment:
    def test_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        self.driver.find_element(By.CSS_SELECTOR,"span[role='presentation']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[role='searchbox']").send_keys("a")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ul/li[text()='Autumn Harp Business Limited']").click()

        #below Code Fails Why I dont Know ??
       #vendor_list = self.driver.find_elements(By.CSS_SELECTOR, "ul li[role='option']")
       #vendor_list= self.driver.find_elements(By.XPATH,"//ul/li[@role='option']")
       #for vendor in vendor_list:
       #    print(vendor.text)
       #    if vendor.text == "Autumn Harp Business Limited":
       #        vendor.click()
    def test_include_close_checkbox(self):
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        self.driver.find_element(By.CSS_SELECTOR,"label input[type='checkbox']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Search purchase order']").send_keys("96337064")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "// a[text() = 'PO']").click()
        title_po= (self.driver.title)
        assert title_po== "Purchase Order"











