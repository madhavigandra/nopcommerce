import pytest
from selenium import webdriver
from pageObjects import Addcustomer

class SearchCustomer:
    txtbox_email_id= "SearchEmail"
    txtbox_firstname_id= "SearchFirstName"
    txtbox_lastname_id="SearchLastName"
    bttn_search_id="search-customers"

    tbleresults_xpath="//*[@id='customers-grid_wrapper']"
    tble_xpath="//*[@id='customers-grid']"
    tblerows_xpath="//*[@id='customers-grid']/tbody/tr"
    tblcolumns_xpath="//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtbox_email_id).clear()
        self.driver.find_element_by_id(self.txtbox_email_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtbox_firstname_id).clear()
        self.driver.find_element_by_id(self.txtbox_firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtbox_lastname_id).clear()
        self.driver.find_element_by_id(self.txtbox_lastname_id).send_keys(lname)

    def clickonSearch(self):
        self.driver.find_element_by_id(self.bttn_search_id).click()

    def getNoOfColumns(self):
        return len(self.driver.find_element_by_id(self.tblcolumns_xpath))

    def getNoOfRows(self):
        return len(self.driver.find_element_by_id(self.tblerows_xpath))

    def searchCustomerByEmail(self,email):
        flag= False
        for r in range(1, self.getNoOfRows()+1):
           table= self.driver.find_element_by_xpath(self.tble_xpath)
           emailid = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr[" +str(r)+"]/td[2]").text
           if emailid== email:
               flag= True
               break
           return flag

    def searchCustomerByName(self,Name):
     flag= False
     for r in range(1,self.getNoOfRows()+1):
         table= self.driver.find_element_by_xpath(self.tble_xpath)
         name=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
         if name==Name:
            flag= True
            break
         return flag

