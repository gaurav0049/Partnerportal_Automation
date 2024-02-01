import time

from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PP_Automation_Testing.logging.Baseclass import Logging
@pytest.mark.usefixtures('setup')
class Test_product_catalog():
    obj = Logging()  # object Creation
    log= obj.get_logger()
    x_path_product_cat_drop_down= "//ul/li/a/span[text()='Product Catalog']"
    x_path_List_product =  "//ul/li/a/span[text()='List Products']"

    def test_list_product_link_test(self):
        self.driver.find_element(By.XPATH,self.x_path_product_cat_drop_down).click()
        self.driver.find_element(By.XPATH,self.x_path_List_product).click()
        self.driver.find_element(By.XPATH,"//tr[1]/td[2]/a").click()
        self.driver.back()
        self.driver.find_element(By.LINK_TEXT,"12064885").click()
        self.driver.back()
        self.driver.find_element(By.XPATH,"//tr[1]/td[9]/a").click()
    def test_filters(self):
        self.driver.find_element(By.XPATH, self.x_path_product_cat_drop_down).click()
        self.driver.find_element(By.XPATH, self.x_path_List_product).click()
        self.driver.find_element(By.NAME,"filter_name").send_keys("12064885")
        self.driver.find_element(By.XPATH,"//span[text()='All Vendors']").click()
        self.driver.find_element(By.XPATH,"//ul/li[@role='option'][text()='Aircos Business name']").click()
