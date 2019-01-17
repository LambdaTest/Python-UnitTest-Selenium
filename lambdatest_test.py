import unittest, time, re
import base_test
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
        added_item = driver.find_element_by_xpath("//span[@class='done-false']").text
        print (added_item)
        self.assertEqual ("Yey, Let's add it to list", added_item )
        if added_item in ":
            return True
        else:
            return False

if __name__ == "__main__":
    unittest.main()
