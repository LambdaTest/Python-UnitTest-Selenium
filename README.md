# Python-UnitTest-Selenium
![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
--- 

![logo](https://github.com/Apoorvlt/test/blob/master/logo.PNG)

## Prerequisites for Python Behave tutorial 

### 1. Python Installation

 * [Download Python](https://www.python.org/downloads/) and click on Add to path and install.
 
 * To check if python installed correctly you need to go to terminal type python in command prompt. It will show you the current version you have downloaded.
 
### 2. LambdaTest Credentials
  * To use Pytest with LambdaTest, make sure you have the 2 environment variables LT_USERNAME and LT_ACCESS_KEY set. To obtain a username and access_key, sign up for free [here](https://lambdatest.com). After signing up you can find your username and access key [here](https://accounts.lambdatest.com/detail/profile).
  * In the terminal export your LambdaTest Credentials as environmental variables:
       
       * For Mac/Linux
            ```
            $ export LT_USERNAME=<your LambdaTest username>
            $ export LT_ACCESS_KEY=<your LambdaTest access key>
            ```
       
       * For Windows
            ```
            set LT_USERNAME=<your LambdaTest username>
            set LT_ACCESS_KEY=<your LambdaTest access key>
            ```

### 3. Setup

 * Clone [Python-UnitTest-Selenium](https://github.com/LambdaTest/Python-UnitTest-Selenium.git) from GitHub.
 * Navigate to the cloned directory
 * Install project dependencies by running command:
 
 ```
   pip install -r requirements.txt
 ```
 
 Requirements.txt file includes the following:
 
 ```
ConfigParser
selenium>2.5
pytest
nose
pytest-xdist
```
## Test Scenario

### Single Test

In our demonstration, we will be creating a script that uses the Selenium WebDriver to click check boxes and add button. If assert returns true, it indicates that the test case passed successfully and will show up in the automation logs dashboard else if assert returns false, the test case fails, and the errors will be displayed in the automation logs.

You have successfully configured your project and are ready to execute your first UnitTest selenium testing script. Here is the  file for UnitTest selenium Testing. Lets call it <code>lambdatest_test.py</code>.

```
import unittest, time, re
import base_test
from selenium import webdriver
 
from selenium.webdriver.common.keys import Keys
 
class LambdaTest(base_test.BaseTest):
 
    def test_unit_user_should_able_to_add_item(self):
 
        # try:
 
        driver = self.driver
 
        # Url
 
        driver.get(self.base_url)
 
        # Click on check box
 
        check_box_one = driver.find_element_by_name("li1")
 
        check_box_one.click()
 
        # Click on check box
 
        check_box_two = driver.find_element_by_name("li2")
 
        check_box_two.click()
 
        # Enter item in textfield
 
        textfield = driver.find_element_by_id("sampletodotext")
 
        textfield.send_keys("Yey, Let's add it to list")
 
        # Click on add button
 
        add_button = driver.find_element_by_id("addbutton")
 
        add_button.click()
 
        # Verified added item
 
        added_item = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[6]/span").text
 
        print (added_item)

        #Assertion 
        if "Yey, Let's add it to list" in added_item:
            driver.execute_script("lambda-status=passed")

        else:
            driver.execute_script("lambda-status=failed")
            
        
 

 
if __name__ == "__main__":
 
    unittest.main()

    
 ```
#### To run file  :

```
 python lambdatest_test.py or nosetests lambdatest_test.py
```
 

##  Routing traffic through your local machine using Lambdatest
- Set tunnel value to `True` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)



Below we see a screenshot that depicts our UnitTest code is running over different browsers i.e Chrome, Firefox and Safari on the LambdaTest Selenium Grid Platform. The results of the test script execution along with the logs can be accessed from the LambdaTest Automation dashboard.


![alttext](https://github.com/Apoorvlt/test/blob/master/unitcap.PNG)



### Important Note:
---
- Some Safari & IE browsers, doesn't support automatic resolution of the URL string "localhost". Therefore if you test on URLs like "http://localhost/" or "http://localhost:8080" etc, you would get an error in these browsers. A possible solution is to use "localhost.lambdatest.com" or replace the string "localhost" with machine IP address. For example if you wanted to test "http://localhost/dashboard" or, and your machine IP is 192.168.2.6 you can instead test on "http://192.168.2.6/dashboard" or "http://localhost.lambdatest.com/dashboard".

## About LambdaTest
[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

### Resources

##### [Selenium Documentation](http://www.seleniumhq.org/docs/)

##### [Python Documentation](https://docs.python.org/2.7/)

##### [Pytest Documentation](http://pytest.org/latest/contents.html)
