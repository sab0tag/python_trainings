# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time as t
from group import Group


def open_home_page(driver):
    driver.get("http://localhost:8080/addressbook/index.php")


def login(driver, user, pwd):
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(user)
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(pwd)
    driver.find_element_by_xpath("//input[@value='Login']").click()


def open_groups_page(driver):
    driver.find_element_by_id("container").click()
    driver.find_element_by_link_text("groups").click()


def create_group(driver, group):
    driver.find_element_by_name("new").click()
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    # fill group form
    driver.find_element_by_name("group_name").send_keys(group.groupName)
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys(group.headerDescr)
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys(group.footerDescr)
    # submit group creation
    driver.find_element_by_name("submit").click()


def return_to_groups_page(driver):
    driver.find_element_by_link_text("group page").click()


def logout(driver):
    driver.find_element_by_link_text("Logout").click()


class add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_new_group(self):
        driver = self.driver
        open_home_page(driver)
        t.sleep(2)
        login(driver, user="admin", pwd="secret")
        open_groups_page(driver)
        create_group(driver, Group(groupName="newGroup", headerDescr="header description", footerDescr="footer description"))
        return_to_groups_page(driver)
        logout(driver)

    def test_empty_group(self):
        driver = self.driver
        open_home_page(driver)
        t.sleep(2)
        login(driver, user="admin", pwd="secret")
        open_groups_page(driver)
        create_group(driver, Group(groupName="", headerDescr="", footerDescr=""))
        return_to_groups_page(driver)
        logout(driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
