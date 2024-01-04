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

obj=Logging()
@pytest.mark.usefixtures('setup')
class Test_Pomangment():

    log=obj.get_logger()
    x_path_of_pom= "//a[@title='Purchase Order Management']"
    x_path_of_po="//a[@title='Purchase Orders']"

    def test_button(self):
        #log = self.get_logger()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//a[@title='Purchase Order Management']").click()
        self.log.info("Po Management Button check")
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        self.log.info("Purchase order button check")
        self.driver.find_element(By.CSS_SELECTOR,"span[role='presentation']").click()
        self.log.info("Dropdown Check Successfully of vendor")
        self.driver.find_element(By.CSS_SELECTOR, "input[role='searchbox']").send_keys("a")
        self.log.info("Vendor input Area field check")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//ul/li[text()='AUTUMN HARP BUSINESS LIMITED']").click()
        self.log.info("Dropdown Check Successfully")


        #below Code Fails Why I dont Know ??
       #vendor_list = self.driver.find_elements(By.CSS_SELECTOR, "ul li[role='option']")
       #vendor_list= self.driver.find_elements(By.XPATH,"//ul/li[@role='option']")
       #for vendor in vendor_list:
       #    print(vendor.text)
       #    if vendor.text == "Autumn Harp Business Limited":
       #        vendor.click()
    def test_include_close_checkbox(self):
        #log = self.get_logger()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        self.driver.find_element(By.CSS_SELECTOR,"label input[type='checkbox']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Search purchase order']").send_keys("96337064")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "// a[text() = 'PO']").click()
        title_po = (self.driver.title)
        assert title_po == "Purchase Order"
        self.log.info("checked Closed Box")

    def test_create_po(self):
        wait = WebDriverWait(self.driver, 15)
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
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#product_quantity_28308').send_keys('12.34')
        self.driver.find_element(By.CSS_SELECTOR, '#product_quantity_33040').send_keys('24.56')
        #try:
        #    for i in range(1,10):
        #       self.driver.find_element(By.XPATH,"//tr[{0}]/td[6]/button".format(i)).click()
        #except:
        #    pass

        adds= self.driver.find_elements(By.CSS_SELECTOR,"td button")
        for add in adds:
            time.sleep(2)
            add.click()

        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div/i[@class='fa fa-shopping-cart']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH,"//tr[1]/td[8]").click()

        self.driver.find_element(By.XPATH, "//ul/li[text()='AirWH']").click()
        time.sleep(6)

        #wait.until(EC.presence_of_element_located((By.XPATH, "//tr[2]/td[8]")))

        self.driver.find_element(By.XPATH, "//tr[2]/td[8]").click()

        self.driver.find_element(By.XPATH, "//ul/li[text()='AirWH']").click()

        wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='submit']")))
        time.sleep(6)

        #for loc in vendor_loc:
        #    time.sleep(5)
        #    action.move_to_element(loc).click().perform()
        #    time.sleep(2)
        #    action.move_to_element(self.driver.find_element(By.XPATH, "//ul/li[text()='AirWH']")).click().perform()
        #time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@name='submit']").click()


        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))

        success_po_create = (self.driver.find_element
                             (By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text)
        assert "created successfully" in success_po_create


    def test_reject_po(self):
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Order Management']").click()
        self.driver.find_element(By.XPATH, "//a[@title='Purchase Orders']").click()
        i = 1
        while True:
            status = self.driver.find_element(By.XPATH, "//tr[{0}]/td[6]/span".format(i)).text

            if status == "Pending" or status == "Pending Approval":
                self.driver.find_element(By.XPATH, "//tr[{0}]/td[10]/a[text()='PO']".format(i)).click()
                break
            else:
                i = i + 1
        self.driver.find_element(By.XPATH, "//button[@name='submit'][normalize-space()='Reject']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH,"//textarea[@name='purchase_order_company_reject_reason']").send_keys("Automated Test Rejection")

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-submit-company-reject-purchase-order-form-with-reason-event']").click()


        wait=WebDriverWait(self.driver,15)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   "//div[@class='alert alert-success alert-dismissible']")))
        success_message = self.driver.find_element(By.XPATH,
                                                   "//div[@class='alert alert-success alert-dismissible']").text

        assert "rejected successfully" in success_message
        print(success_message)

    def test_Close_po(self):
        self.driver.find_element(By.XPATH,self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH,self.x_path_of_po).click()
        i=1
        while True:
            status= self.driver.find_element(By.XPATH,"//tr[{0}]/td[6]/span".format(i)).text

            if status== "Pending" or status== "Pending Approval":
                self.driver.find_element(By.XPATH,"//tr[{0}]/td[10]/a[text()='PO']".format(i)).click()
                break
            else:
                i = i + 1

        self.driver.find_element(By.XPATH, "//button[text()='Close PO']").click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   "//div[@class='alert alert-success alert-dismissible']")))
        success_message = self.driver.find_element(By.XPATH,
                                                   "//div[@class='alert alert-success alert-dismissible']").text

        assert "closed successfully" in success_message
        print(success_message)






























