import time


import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Dashboard:
    def __init__(self,driver):
        self.driver=driver


    def dashboradlanding(self):
        #action = ActionChains(self.driver)
        #action.move_to_element(self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")).perform()
        #action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "[title='Company']")).click().perform()
        #self.driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(getdata["username"])
        #self.driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(getdata["password"])
        #self.driver.find_element(By.CSS_SELECTOR, "[name='remember']").click()
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        assert self.driver.title == "Dashboard"

    def dashboardcheck(self):
        self.driver.implicitly_wait(5)
        date_filter= Select(self.driver.find_element(By.CSS_SELECTOR,"#ChoosePastHistory"))
        date_filter.select_by_visible_text('Last 3 Months')
        self.driver.find_element(By.CSS_SELECTOR,"[role='textbox']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys('a')
        time.sleep(2)
        variable= self.driver.find_elements(By.XPATH, "//ul/li[@role='option']")
        for vendor in variable:

            if vendor.text == "AUTUMN HARP BUSINESS LIMITED":
                vendor.click()
                break
    def removeselectedvendor(self):
        self.driver.find_element(By.CSS_SELECTOR,"button span").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='textbox']").click()


    def dashboardtext(self):
        message= self.driver.find_element(By.TAG_NAME,'h2').text
        assert  message == "Good Morning" or message == "Good Afternoon" or message== "Good Evening"

    def customoption(self):
        date_filtercc = Select(self.driver.find_element(By.CSS_SELECTOR, "#ChoosePastHistory"))
        date_filtercc.select_by_visible_text('Custom Option')
        self.driver.find_element(By.CSS_SELECTOR, "[name='customDateFilter']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[name='customDateFilter']").send_keys("01/14/2024 - 01/25/2024")


    def customoption_check(self):
        self.driver.implicitly_wait(5)
        month_Year_left= "Feb 2023"
        month_year_right="Sep 2023"
        date_filtercc = Select(self.driver.find_element(By.CSS_SELECTOR, "#ChoosePastHistory"))
        date_filtercc.select_by_visible_text('Custom Option')


        self.driver.find_element(By.CSS_SELECTOR, "[name='customDateFilter']").clear()
        #time.sleep(1)
        mon_year = self.driver.find_element(By.CSS_SELECTOR, "div[class='drp-calendar left'] th[class='month']").text


        while True:
           mon_year_left = self.driver.find_element(By.CSS_SELECTOR,
                                               "div[class='drp-calendar left'] th[class='month']").text
           print(mon_year)
           if month_Year_left == mon_year_left:
               self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[3]").click()
               break
           else:
               self.driver.find_element(By.XPATH, "//th[@class='prev available']").click()

        while True:
            mon_year_right= (self.driver.find_element
                             (By.CSS_SELECTOR, "div[class='drp-calendar right'] th[class='month']").text)
            if month_year_right== mon_year_right:
                self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[4]").click()
                break
            else:
                self.driver.find_element(By.XPATH, "//th[@class='next available']").click()

        self.driver.find_element(By.XPATH, '//button[text()="Apply"]').click()

    def vendor_acitivity(self):
        #Scrolling to target element :-
        try:
            target = self.driver.find_element(By.XPATH, "//a[text()='Load More']")
            action=ActionChains(self.driver)
            action.move_to_element(target).click().perform()
            time.sleep(2)
            target = self.driver.find_element(By.XPATH, "//a[text()='Load More']")
            action.move_to_element(target).click().perform()
        except:
            print ("Load More found")
        #self.driver.execute_script('arguments[0].scrollIntoView(true);', target)

    #@pytest.fixture(params=[{"username": "vibinguniverse", "password": "Admin@123"}
    #                        ])
    #def getdata(self, request):
    #    return request.param

    # <-----------------------Dasboard END--------------------->





































