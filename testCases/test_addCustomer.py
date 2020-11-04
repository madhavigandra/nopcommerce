import random
import string
import itertools
from utilities.readproperties import ReadConfig
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Addcustomer import AddCustomer
from pageObjects.LoginPage import LogInPage
import pytest
from selenium import webdriver

class Test003Addcustomer:
    baseURL = ReadConfig.readApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # create logger object

    def test_addCustomer(self):
        self.logger.info("**************test003  add customer  Login started*****")
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # login data is passed using the login page class object lp
        self.lp = LogInPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.logger.info("************test 003: login successfull************")
        self.logger.info("******** Now adding new customer test started ***************")
        # adding customer information after the successful login
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.addNew()
        self.logger.info("****** adding customer details*************")
        # generate a random gmail for each customer
        # 8 character string  in lowercase with digits
        def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            # loop to generate each random character for gmail
            return ''.join(random.choice(chars) for x in range(size))

        self.email = random_generator()
        self.addcust.setCustomerEmail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Maddie")
        self.addcust.setLastName("Gandra")
        self.addcust.setDob("07/01/1979")
        self.addcust.setCompanyname("AutomationQA")
        self.addcust.setNewsLetter("My NOP commerce project")
        self.addcust.setAdminContent(" This is for testing")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerOfVendor("1")
        self.addcust.clickSave()

        self.logger.info("************ saving customer information*****************")

        self.logger.info("************* add customer validation started********")
        # a message about the customer added successfully is displayed on the body of page.so capture it
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add customer test passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scrnshot.png")
            self.logger.error("*************** add customer  Test Failed *************")
            assert True == False
        self.driver.close()
        self.logger.info(" ******** Ending test003 Add customer test **************")

