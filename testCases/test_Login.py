from selenium import webdriver
from pageObjects.LoginPage import LogInPage
import pytest
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test001login:
    baseurl = ReadConfig.readApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("**************************Test_001_login************************************")
        self.logger.info("**************************verifying Home Page Title***********************************")
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            self.logger.info("************************Home page verification test Passed***************************")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\gandra\\PycharmProjects\\NOPCommerceApp\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************************Home page verification test Failed***************************")

            assert False

    def test_login(self):
        self.logger.info("**************************Test_001_login************************************")
        self.logger.info("**************************verifying Home Page Login***********************************")
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get(self.baseurl)
        self.lp = LogInPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        title = self.driver.title
        self.lp.clickLogOut()
        self.driver.close()
        if title == "Dashboard / nopCommerce administration":
            self.logger.info("************************Home page Login test Passed***************************")
            assert True
        else:
            self.logger.error("************************Home page Login test Failed***************************")
            self.driver.save_screenshot("C:\\Users\\gandra\\PycharmProjects\\NOPCommerceApp\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
