import time


import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PP_Automation_Testing.Modules_Of_Partner_Portal.Dashboard_Objects import Dashboard
from PP_Automation_Testing.logging.Baseclass import Logging

@pytest.mark.usefixtures('setup')
class Test_all:
    log= Logging().get_logger()


    def test_dashboard(self):
        self.log.info("Dashboard Testing")
        self.obj1=Dashboard(self.driver)

        self.obj1.dashboradlanding()
        self.obj1.dashboardcheck()
        self.obj1.removeselectedvendor()
        self.obj1.dashboardtext()
        self.obj1.customoption()
        self.obj1.customoption_check()
        self.obj1.vendor_acitivity()