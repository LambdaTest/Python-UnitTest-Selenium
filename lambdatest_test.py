import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        lt_options = {
            "user": username,
            "accessKey": access_key,
            "build": "UnitTest-Selenium-Sample",
            "name": "UnitTest-Selenium-Test",
            "platformName": "MacOS Ventura",
            "w3c": True,
            "browserName": "Edge",
            "browserVersion": "latest-2",
            "selenium_version": "4.8.0"
        }
        
        browser_options = EdgeOptions()
        browser_options.set_capability('LT:Options', lt_options)
  
        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)


# tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Click on check box
        check_box_one = driver.find_element(By.NAME,"li1")
        check_box_one.click()

        # Click on check box
        check_box_two = driver.find_element(By.NAME,"li2")
        check_box_two.click()

        #Take Smart UI screenshot
        #driver.execute_script("smartui.takeScreenshot")

        # Enter item in textfield
        textfield = driver.find_element(By.ID,"sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        add_button = driver.find_element(By.ID,"addbutton")
        add_button.click()

        # Verified added item
        added_item = driver.find_element(By.XPATH,
            "//span[@class='done-false']").text
        print(added_item)


if __name__ == "__main__":
    unittest.main()
