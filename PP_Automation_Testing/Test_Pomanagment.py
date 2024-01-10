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


@pytest.mark.usefixtures('setup')
class Test_Pomangment():
    obj = Logging()  # object Creation
    log=obj.get_logger()
    x_path_of_pom= "//a[@title='Purchase Order Management']"
    x_path_of_po="//a[@title='Purchase Orders']"
    exportButton="div button[title='Export']"
    x_path_shipment="//span[normalize-space()='Shipments']"
    Css_item_receipt="[title='Item Receipts']"



    def test_button(self):
        #log = self.get_logger()
        self.driver.implicitly_wait(10)
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
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
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

        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='submit']")))
        time.sleep(6)

        # for loc in vendor_loc:
        #    time.sleep(5)
        #    action.move_to_element(loc).click().perform()
        #    time.sleep(2)
        #    action.move_to_element(self.driver.find_element(By.XPATH, "//ul/li[text()='AirWH']")).click().perform()
        # time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
        success_po_create = (self.driver.find_element
                             (By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text)
        assert "created successfully" in success_po_create

    def test_reject_po(self):
        self.driver.find_element(By.XPATH,self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH,self.x_path_of_po).click()
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

    def test_ExportButton(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
        self.driver.find_element(By.CSS_SELECTOR,self.exportButton).click()
        self.log.info("Export Button Tested")
    def test_check_IR_Button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
        IRS=self.driver.find_elements(By.XPATH,"//tr/td[10]/a[2]")
        for IR in IRS:
            IR.click()
            break
        IR_view=self.driver.find_elements(By.XPATH,"//tr/td[9]/a")
        for single_IR in IR_view:
            single_IR.click()
            break
        self.log.info("IR and View Button Checked")

    def test_po_wise_View_button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()

        i = 1

        while True:
            for i in range(1,26):
                po_number = self.driver.find_element(By.XPATH, "//tr[{0}]/td[3]".format(i)).text

                if po_number == "36006008":
                    self.driver.find_element(By.XPATH, "//tr[{0}]/td[10]/a[2]".format(i)).click()
                    break

            if po_number== "36006008":
                break
            NextButton = self.driver.find_element(By.XPATH, "//a[normalize-space()='Next']")
            self.driver.execute_script("arguments[0].scrollIntoView();", NextButton)
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Next']").click()

        #po_numbers = self.driver.find_elements(By.XPATH, "//tr")
        #for po_num in po_numbers:
        #    po_No= po_num.find_element(By.XPATH,"td[3]").text
        #    if po_No== "PO70014604258":
        #        po_num.find_element(By.XPATH,"td[10]/a[2]").click()
        #    break

    def test_check_po_id_link(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
        po_id= self.driver.find_element(By.XPATH,"//tr[1]/td[2]/a")
        po_number_list_page=po_id.text
        po_id.click()
        po_num_detail_page=self.driver.find_element(By.TAG_NAME,'h1').text
        assert po_number_list_page in po_num_detail_page
        self.log.info("The Po link Checked")

    def test_receive_button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
        Receives = self.driver.find_elements(By.XPATH, "//tr/td[10]/a[2][text()='Receive']")
        for receive in Receives:
            receive.click()
            receive_button=self.driver.find_element(By.XPATH,"//a[text()='Receive Item']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);",receive_button)
            receive_button.click()
            break
        input_box=self.driver.find_element(By.XPATH,"//tr[1]/td[4]/input")
        input_box.clear()
        input_box.send_keys("1.23")

    def test_document_download(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_of_po).click()
        Receives = self.driver.find_elements(By.XPATH, "//tr/td[10]/a[2][text()='Receive']")
        for receive in Receives:
            receive.click()
            document_button= self.driver.find_element(By.XPATH,"//tr[1]/td[10]/button")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", document_button)
            document_button.click()
            self.driver.find_element(By.XPATH,"//tr[1]/td[3]/a").click()
            self.driver.find_element(By.XPATH,"//div[@id='vendor-sale-shipping-order-documents-modal']//button[@type='button'][normalize-space()='×']").click()
            self.log.info("Document download button check")
            break

    def test_shipment(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_shipment).click()
        self.driver.find_element(By.CSS_SELECTOR,"#select2-shipment_vendor_list-container").click()
        self.driver.find_element(By.XPATH,"//span/span/span/input").send_keys("air")
        self.driver.find_element(By.XPATH,"//ul/li[text()='Aircos Business name']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//tr[1]/td[3]/a").click()
        self.driver.back()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tr[1]/td[4]/a").click()
        self.driver.back()
        search= self.driver.find_element(By.CSS_SELECTOR,"label input")
        search.send_keys("135")
        search.clear()

        self.driver.find_element(By.XPATH,"//tr/td[11]/button").click()
        self.driver.find_element(By.XPATH,"//button[@aria-label='Close']").click()
        self.driver.find_element(By.XPATH,"//tr/td[11]/a").click()

    def test_view_page_Button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_shipment).click()
        #status=self.driver.find_element(By.XPATH,"//tr[1]/td[10]").text
        #print(status)
        i=1
        while True:
            while True:
                status=self.driver.find_element(By.XPATH,"//tr[{0}]/td[10]".format(i)).text
                if status=="Shipped":
                    self.driver.find_element(By.XPATH,"//tr[{0}]/td[11]/button".format(i)).click()
                    break
                else:
                    i=i+1

            if status == "Shipped":
                break
            nextpage = self.driver.find_element(By.XPATH, "(//a[@href='#'])[9]")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", nextpage)
            nextpage.click()

    def test_view_bill_Button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_shipment).click()
        #status=self.driver.find_element(By.XPATH,"//tr[1]/td[10]").text
        #print(status)
        i=1
        while True:
            for i in range(1,11):
                status=self.driver.find_element(By.XPATH,"//tr[{0}]/td[10]".format(i)).text
                if status=="Shipped":
                    self.driver.find_element(By.XPATH,"//tr[{}]/td[11]/a/span[normalize-space()='Bill']".format(i)).click()
                    break
                else:
                    continue

            if status == "Shipped":
                break
            nextpage = self.driver.find_element(By.XPATH, "(//a[@href='#'])[9]")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", nextpage)
            nextpage.click()

    def test_view_Variance_Button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_shipment).click()
    #    #status=self.driver.find_element(By.XPATH,"//tr[1]/td[10]").text
    #    #print(status)
    #    i=1
    #    for j in range(4):
    #        for i in range(1,11):
    #            try:
    #                varbutton=self.driver.find_element(By.XPATH, "//tr[{}]/td[11]/a/span[text()='Variance']".format(i))
    #                self.driver.execute_script('arguments[0].scrollIntoView(true);',varbutton)
    #                varbutton.click()
    #            except:
    #                continue

            #    else:
            #        continue
#
            #if self.driver.find_element(By.TAG_NAME,'h4').text=="Received Items":
            #   break
            #else:
        nextpage = self.driver.find_element(By.XPATH, "(//a[@href='#'])[9]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", nextpage)
        nextpage.click()

    def test_check_Variance_Button(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.XPATH, self.x_path_shipment).click()
        element=self.driver.find_element(By.XPATH, "//tr[9]/td[11]/a/span[text()='Variance']")
        self.driver.execute_script('arguments[0].scrollIntoView(true);',element)
        print(element.is_displayed())

    def test_check_item_receipt(self):
        self.driver.find_element(By.XPATH, self.x_path_of_pom).click()
        self.driver.find_element(By.CSS_SELECTOR,self.Css_item_receipt).click()
        for i in range(1,26):
            po_id= self.driver.find_element(By.XPATH,"//tr[{}]/td[2]/a".format(i)).text
            self.driver.find_element(By.XPATH, "//tr[{}]/td[2]/a".format(i)).click()

            self.driver.back()

            ir_number= self.driver.find_element(By.XPATH,"//tr[{}]/td[3]/a".format(i)).text
            self.driver.find_element(By.XPATH, "//tr[{}]/td[3]/a".format(i)).click()

            self.driver.back()
            self.driver.find_element(By.XPATH, "//tr[{}]/td[9]/a".format(i)).click()

            heading= self.driver.find_element(By.TAG_NAME,'h1').text
            break

        self.log.info("Details check")
        print(po_id,ir_number,heading)
        assert po_id in heading
        assert ir_number in heading






































































