import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class Test_Login():
    def test_URL(self):
        self.driver.get("https://www.partnerportal.ai/")
        #self.driver.


    #driver.implicitly_wait(10)
    #action = ActionChains(driver)
    #action.send_keys(Keys.CONTROL).send_keys(Keys.SUBTRACT).perform()
    #action.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")).perform()
    #action.move_to_element(driver.find_element(By.CSS_SELECTOR, "[title='Company']")).click().perform()
    #driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys("vibinguniverse")
    #driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("Admin@123")
    #driver.find_element(By.CSS_SELECTOR, "[name='remember']").click()
    #driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()