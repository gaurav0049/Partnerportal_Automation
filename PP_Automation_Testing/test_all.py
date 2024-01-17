import time

from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PP_Automation_Testing.Baseclass import Logging
from PP_Automation_Testing.Test_Dashboard import Test_Dashboard
from PP_Automation_Testing.Test_Pomanagment import Test_Pomangment


@pytest.mark.usefixtures('setup')
class Test_all:
    obj1 = Test_Pomangment()
    obj2 = Test_Dashboard()
    def test_all(self):
        self.obj1.test_button()

