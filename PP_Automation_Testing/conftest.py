import calendar

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope='class')
def setup(request):
    option= webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver= webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("https://www.partnerportal.ai/")
    driver.implicitly_wait(10)
    action = ActionChains(driver)
    action.send_keys(Keys.CONTROL).send_keys(Keys.SUBTRACT).perform()
    action.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")).perform()
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "[title='Company']")).click().perform()
    driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys("vibinguniverse")
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("123123")
    driver.find_element(By.CSS_SELECTOR, "[name='remember']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    request.cls.driver = driver






    #yield
    #driver.quit()



    #current_datetime = datetime.now()
    #current_year = current_datetime.strftime("%Y")
    ##print(current_year)
    #month_num=current_datetime.strftime("%m")
    #month_name = calendar.month_name[int(month_num)]
    #mon_name_year= (month_name[0:3]+" "+current_year)
    #request.cls.mon_name_year= mon_name_year





