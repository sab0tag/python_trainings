# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_login_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/addressbook/index.php")

    def login(self, username, password):
        driver = self.driver
        self.open_login_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def add_usr(self, name, surname, nick, titl, company_name, street, mobile_number, email_1, email_2, b_day,
                b_month, b_year, street2):
        driver = self.driver
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
        self.return_to_home_page(driver)

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home page").click()

    def logout(self):
        driver = self.driver
        # logout part
        driver.find_element_by_link_text("Logout").click()

    def test_add_user(self):
        driver = self.driver
        self.login(username="admin", password="secret")
        self.add_usr(name="Igor", surname="Petrenko", nick="sab0tag", titl="QA Engineer", company_name="Luxoft",
                     street="Mayakovskogo avenue", mobile_number="+380661530460", email_1="sabotag1985@gmail.com",
                     email_2="ihor.petrenko@yahoo.com", b_day="2", b_month="November", b_year="1985", street2="Lenina")
        self.logout()

    def test_add_empty_user(self):
        driver = self.driver
        self.login(username="admin", password="secret")
        self.add_usr(name="", surname="", nick="", titl="", company_name="",
                     street="", mobile_number="", email_1="",
                     email_2="", b_day="", b_month="", b_year="", street2="")
        self.return_to_home_page()
        self.logout()

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
