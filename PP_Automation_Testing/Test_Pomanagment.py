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
        self.driver.find_element(By.XPATH,"//ul/li[text()='AUTUMN HARP BUSINESS LIMITED']").click()

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
        title_po = (self.driver.title)
        assert title_po == "Purchase Order"

    def test_create_po(self):
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Create PO']").click()
        self.driver.find_element(By.CSS_SELECTOR,"#select2-vendor_id-container").click()
        time.sleep(1)
        vendors_po=self.driver.find_elements(By.CSS_SELECTOR,"ul li[role='option']")
        for vendor in vendors_po:
            if vendor.text == "Aircos Business name":
                vendor.click()
                break

                #self.driver.find_element(By.CSS_SELECTOR, '#select2-input-manufracturer-container').click()
                #manufacturers = self.driver.find_elements(By.XPATH,"//span/ul/li")
                #for manufactur in manufacturers:
                #    if manufactur.text == "Laura mercier":
                #        manufactur.click()
                #        break
        self.driver.find_element(By.CSS_SELECTOR, '#select2-input-manufracturer-container').click()
        self.driver.find_element(By.XPATH, "//ul/li[text()='Laura mercier']").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@title='Select Brand(s)']").click()
        self.driver.find_element(By.XPATH, "//ul/li[1]/a/label/input").click()

        self.driver.find_element(By.CSS_SELECTOR, '''button[title="laura mercier'S"]''').click()


















