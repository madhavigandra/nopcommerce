import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# add customer page
class AddCustomer:
    lnkCustomers_menu_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/a"
    lnkCustomers_menuitem_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    lnk_addnewbutton_xpath="/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    txtbox_email_xpath=" //*[@id='Email']"
    txtbox_password_xpath="//*[@id='Password']"
    txtbox_firstname_xpath="//*[@id='FirstName']"
    txtbox_lastname_xpath ="//*[@id='LastName']"
    rd_gendermale_xpath= "//*[@id='Gender_Male']"
    rd_genderfemale_xpath = "//*[@id='Gender_Female']"
    txtbox_dateofbirth_xpath="//*[@id='DateOfBirth']"
    txtbox_companyname_xpath= "//*[@id='Company']"
    lst_customerroles_xpath="//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    lstitem_administrators_xpath= "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitem_forummoderators_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitem_guests_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitem_registered_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstitem_vendors_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    drpdown_managerofvendor_xpath= "//*[@id='VendorId']"
    txtbox_admincontent_xpath="//*[@id='AdminComment']"
    lst_unregister_xpath="//*[@id='SelectedCustomerRoleIds_taglist']"
    link_save_xpath="/html/body/div[3]/div[3]/div/form/div[1]/div/button[1]"
    txtbox_newsletter_xpath= "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div/input"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
       self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()


    def clickOnCustomerMenuItem(self):
       self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def addNew(self):
            self.driver.find_element_by_xpath(self.lnk_addnewbutton_xpath).click()

    def setCustomerEmail(self, email):
                self.driver.find_element_by_xpath(self.txtbox_email_xpath).send_keys(email + "@gmail.com")

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txtbox_password_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtbox_firstname_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtbox_lastname_xpath).send_keys(lastname)

    def setGender(self, gender):
       if gender=="Female":
           self.driver.find_element_by_xpath(self.rd_genderfemale_xpath).click()
       elif gender == "Male":
            self.driver.find_element_by_xpath(self. rd_gendermale_xpath).click()
       else:
           self.driver.find_element_by_xpath(self.rd_genderfemale_xpath).click()
    def setDob(self,dob):
      self.driver.find_element_by_xpath(self.txtbox_dateofbirth_xpath).send_keys(dob)

    def  setCompanyname(self,companyname):
       self.driver.find_element_by_xpath(self.txtbox_companyname_xpath).send_keys(companyname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.lst_customerroles_xpath).click()
        time.sleep(3)
        if role == 'Administrators':
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_administrators_xpath)
        elif role == 'Forum Moderators':
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_forummoderators_xpath)
        elif role == 'Registered':
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_registered_xpath)
        elif role == 'Guests':
             time.sleep(3)
             self.driver.find_element_by_xpath(self.lst_unregister_xpath).click()
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_guests_xpath)
        elif role == 'Vendors':
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_vendors_xpath)
        else:
             self.listitem = self.driver.find_element_by_xpath(self.lstitem_guests_xpath)
             time.sleep(3)
           #self.listitem.click() unstead of using this method , we use following method of javascript
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpdown_managerofvendor_xpath))
        drp.select_by_value(value)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtbox_admincontent_xpath).send_keys(content)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.link_save_xpath).click()

    def setNewsLetter(self,news):
         self.driver.find_element_by_xpath(self.txtbox_newsletter_xpath).send_keys(news)

