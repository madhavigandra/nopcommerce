import  pytest
import time
from selenium import webdriver
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LogInPage
from pageObjects.Addcustomer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig

class Test_searchCustomerName005:
    baseURL= ReadConfig.readApplicationURL()
    username= ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen()
    def test_searchCustomerByEmail(self):

        self.logger.info("*********** search customer test 005 started***************")
        self.logger.info("*********** logging with username and password******")
        self.driver= webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LogInPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.logger.info("**********user logged in to website successfully")

        self.logger.info("*********** search customer by mail or name started")
        self.addcust= AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("********** serach customer by email")
        searchcust= SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName(" Lindgren")
        searchcust.clickonSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Brenda Lindgren")
        assert True== status
        self.logger.info("************ test search customer by email finished********")
        self.driver.close()

