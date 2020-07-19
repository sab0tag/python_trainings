# -*- coding: utf-8 -*-
# вспомогательные методы тестового класса
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/addressbook/index.php")

    def login(self, user, pwd):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(pwd)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
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
        self.return_to_groups_page()

    # add a new contact
    def add_usr(self, usr):
        driver = self.driver
        # create a new user
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(usr.name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(usr.surname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(usr.nick)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(usr.titl)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(usr.company_name)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(usr.street)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(usr.mobile_number)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(usr.email_1)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(usr.email_2)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(usr.b_day)
        driver.find_element_by_name("bmonth").click()
        # Select(driver.find_element_by_name("bmonth")).select_by_visible_text(usr.b_month)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(usr.b_year)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(usr.street2)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home page").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.driver.quit()
