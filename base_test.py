from selenium import webdriver
import unittest
import os
from configparser import ConfigParser
caps={}

class BaseTest(unittest.TestCase):

    # ======================================================================
    #            Setup and tear down functions
    # ======================================================================
    @classmethod
    def setUpClass(self):

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.config = ConfigParser()
        my_file = ROOT_DIR + '\config.cfg'
        self.config.read(my_file)
        self.init_capabilities(self)
        self.base_url = "https://lambdatest.github.io/sample-todo-app/"
      
        remote_url= "https://"+self.user_name+":"+self.app_key+"@hub.lambdatest.com/wd/hub"

        caps['name'] = "LambdaTestSampleApp"
        caps['build'] = "PythonUnitTestSample"
        caps['browserName'] = self.browser       
        caps['version'] = self.browser_version
        caps['platform'] = self.os
        caps['network'] = True
        caps['visual']= True
        caps['video']= True
        caps['console']= True

        self.driver = webdriver.Remote(command_executor=remote_url,desired_capabilities=caps)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # open application url
        self.driver.get(self.base_url)

    @classmethod
    def tearDownClass(self):
        print ( "closed browser" )
        self.driver.quit()

    def init_capabilities(self):
        print ("Preparing capabilities")       
        if os.getenv('LT_USERNAME', 0) == 0:
            self.user_name = self.config['Environment']['UserName']
        if os.getenv('LT_APPKEY', 0)  == 0:
             self.app_key = self.config['Environment']['AppKey']
        if os.getenv('LT_OPERATING_SYSTEM', 0) == 0:
             self.os = self.config['Environment']['OS']
        if os.getenv('LT_BROWSER', 0)  == 0:
             self.browser = self.config['Environment']['Browser']
        if os.getenv('LT_BROWSER_VERSION', 0)  == 0:
             self.browser_version = self.config['Environment']['BrowserVersion']
    


