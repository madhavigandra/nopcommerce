from selenium import webdriver
from pageObjects.LoginPage import LogInPage
import pytest
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLSutilities
import time

class Test002ddtlogin:
    baseurl = ReadConfig.readApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    def test_login(self):
        self.logger.info("**************************Test_002_Datadriventest_login************************************")
        self.logger.info("**************************verifying Home Page Login***********************************")
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get(self.baseurl)
        self.lp = LogInPage(self.driver)
        self.rows=XLSutilities.getrowcount(self.path,'sheet1')
        print("number of rows in excel sheet are",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=  XLSutilities.readData(self.path,'sheet1',r,1)
            self.pwd= XLSutilities.readData(self.path,'sheet1',r,2)
            self.result= XLSutilities.readData(self.path,'sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogIn()
            time.sleep(5)
            act_title=self.driver.title
            exp_title= "Dashboard / nopCommerce administration"
            if act_title == exp_title:
               if self.result== "Pass" :   #title passed and the uname and pwd are valid test passes
                self.logger.info("*****test passed")
                self.lp.clickLogOut()
                lst_status.append("Pass")
               elif self.result=='Fail':   # title passed, uname and pwd are invalid test should fail
                self.logger.info("******failed")
                self.lp.clickLogOut()
                lst_status.append("Fail")

            elif act_title != exp_title:
              if self.result=="Pass":     # title not passed,uname and pwd are valid test should fail
                  self.logger.info("****8Failed")
                  lst_status.append("Fail")
              else:
                   self.logger.info("*****Passed")
                   lst_status.append("Pass") # title not passed, invalid data ,test should fail here

        if "Fail" not in lst_status:
            self.logger.info("******Login DDT test passed *****")
            self.driver.close()
            assert True
        else:
             self.logger.info("******* Login DDT test failed")
             self.driver.close()
             assert False
        self.logger.info("******* end of Login test***********")
        self.logger.info("***************completed testcase Login DDT*******")
