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





