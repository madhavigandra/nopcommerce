import configparser

config= configparser.RawConfigParser()
config.read("C:\\Users\\gandra\\PycharmProjects\\NOPCommerceApp\\Configurations\\config.ini")

class ReadConfig:
     @staticmethod
     def readApplicationURL():
         url= config.get('commoninfo','baseurl')
         return url

     @staticmethod
     def getUseremail():
               uname= config.get('commoninfo','username')
               return uname

     @staticmethod
     def getPassword():
            pwd = config.get('commoninfo','password')
            return pwd