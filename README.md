# Python-UnitTest-Selenium
![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
--- 

### Environment Setup

1. Global Dependencies   
   
   -Windows
   * Download the latest python installer for Windows: http://sourceforge.net/projects/pywin32/files/pywin32/
   * Run the installer and follow the setup wizard to install Python
   
   -Linux/Mac
   * Run python --version to see which python version is currently installed, make sure it is 2.5.X or above.
   * OS X, Ubuntu and most other Linux distro's come with Python pre-installed.
   
2. Lambdatest Credentials
    * Set LambdaTest username and access key in environment variables. It can be obtained from [LambdaTest dashboard](https://automation.lambdatest.com/)    
    example:
    - For linux/mac
    ```
    export LT_USERNAME="YOUR_USERNAME"
    export LT_ACCESS_KEY="YOUR ACCESS KEY"
    
    ```
    - For Windows
    ```
    set LT_USERNAME="YOUR_USERNAME"
    set LT_ACCESS_KEY="YOUR ACCESS KEY"
    
    ```
3. Setup
    * Clone [Python-UnitTest-Selenium](https://github.com/LambdaTest/Python-UnitTest-Selenium.git) from GitHub.
    * Navigate to the cloned directory
    * Install project dependencies by running command `pip install -r requirements.txt`
    
4. Running Tests
    * To Start Test:
    - Navigate to Python-UnitTest-Selenium
    - Run following command
    * Execution
    ```
    $ python lambdatest_test.py or nosetests test_sample.py
    ```

#####  Routing traffic through your local machine
- Set tunnel value to `true` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)

### Important Note:
Some Safari & IE browsers, doesn't support automatic resolution of the URL string "localhost". Therefore if you test on URLs like "http://localhost/" or "http://localhost:8080" etc, you would get an error in these browsers. A possible solution is to use "localhost.lambdatest.com" or replace the string "localhost" with machine IP address. For example if you wanted to test "http://localhost/dashboard" or, and your machine IP is 192.168.2.6 you can instead test on "http://192.168.2.6/dashboard" or "http://localhost.lambdatest.com/dashboard".

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

### Resources

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)
##### [UnitTest Documentation](https://docs.python.org/2/library/unittest.html)
