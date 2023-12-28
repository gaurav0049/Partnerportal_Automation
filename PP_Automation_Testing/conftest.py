import calendar

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime


@pytest.fixture(scope='class')
def setup(request):
    option= webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver= webdriver.Chrome(options=option)
    driver.get("https://www.partnerportal.ai/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")).perform()
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "[title='Company']")).click().perform()
    driver.find_element(By.CSS_SELECTOR,"[name='username']").send_keys("vibinguniverse")
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("Admin@123")
    driver.find_element(By.CSS_SELECTOR, "[name='remember']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    request.cls.driver= driver
    #yield
    #driver.quit()



    #current_datetime = datetime.now()
    #current_year = current_datetime.strftime("%Y")
    ##print(current_year)
    #month_num=current_datetime.strftime("%m")
    #month_name = calendar.month_name[int(month_num)]
    #mon_name_year= (month_name[0:3]+" "+current_year)
    #request.cls.mon_name_year= mon_name_year





