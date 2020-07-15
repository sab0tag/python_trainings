# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_login_page(self, driver):
        driver.get("http://localhost:8080/addressbook/index.php")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def add_usr(self, driver, name, surname, nick, titl, company_name, street, mobile_number, email_1, email_2, b_day,
                b_month, b_year, street2):
        # create a new user
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(surname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(nick)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(titl)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(company_name)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(street)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mobile_number)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email_1)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(email_2)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(b_day)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(b_month)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(b_year)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(street2)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def logout(self, driver):
        # logout part
        driver.find_element_by_link_text("Logout").click()

    def add_user(self):
        driver = self.driver
        self.open_login_page(driver)
        self.login(driver, username="admin", password="secret")
        self.add_usr(driver, name="Igor", surname="Petrenko", nick="sab0tag", titl="QA Engineer", company_name="Luxoft",
                     street="Mayakovskogo avenue", mobile_number="+380661530460", email_1="sabotag1985@gmail.com",
                     email_2="ihor.petrenko@yahoo.com", b_day="2", b_month="November", b_year="1985", street2="Lenina")
        self.return_to_home_page(driver)
        self.logout(driver)

    def add_user(self):
        driver = self.driver
        self.open_login_page(driver)
        self.login(driver, username="admin", password="secret")
        self.add_usr(driver, name="", surname="", nick="", titl="", company_name="",
                     street="", mobile_number="", email_1="",
                     email_2="", b_day="", b_month="", b_year="", street2="")
        self.return_to_home_page(driver)
        self.logout(driver)

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


if __name__ == "__main__":
    unittest.main()
