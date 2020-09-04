from model.usr import User
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/index.php")):
            driver.find_element_by_link_text("home").click()

    # call method after the contact has been added
    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def create_contact(self, usr):  # add a new contact
        driver = self.app.driver
        self.open_contact_page()
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(usr)
        driver.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contacts_by_index(index)
        # open modification form by clicking on pencil icon
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit action
        driver.find_element_by_xpath("//input[@name='update'][2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contact_by_id(id)
        # open modification form by clicking on pencil icon
        driver.find_element_by_css_selector("a[href='edit.php?id=%s" % id).click()
        self.fill_contact_form(new_contact_data)
        # submit action
        driver.find_element_by_xpath("//input[@name='update'][2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, usr):
        self.change_field_value("firstname", usr.name)
        self.change_field_value("lastname", usr.surname)
        self.change_field_value("nickname", usr.nickname)
        self.change_field_value("title", usr.title)
        self.change_field_value("company", usr.company)
        self.change_field_value("address", usr.address)
        self.change_field_value("home", usr.homephone)
        self.change_field_value("mobile", usr.mobile_number)
        self.change_field_value("work", usr.workphone)
        self.change_field_value("phone2", usr.secondaryphone)
        self.change_field_value("email", usr.email)
        self.change_field_value("email2", usr.email2)
        self.change_field_value("email3", usr.email3)
        self.change_field_value("byear", usr.b_year)
        self.change_field_value("address2", usr.address2)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def select_contacts_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contacts_by_index(index)
        # submit delete procedure
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to.alert.accept()
        driver.find_elements_by_css_selector("div.msgbox")
        self.open_contact_page()
        # driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contact_by_id(id)
        # submit delete procedure
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to.alert.accept()
        driver.find_elements_by_css_selector("div.msgbox")
        self.open_contact_page()
        # driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def count(self):
        driver = self.app.driver
        self.open_contact_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    # get contacts list method; read the table on the main page
    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contact_page()
            self.contact_cache = []
            for element in driver.find_elements_by_css_selector("tr:nth-child(n+2)"):
                cells = element.find_elements_by_tag_name("td")
                _id = element.find_element_by_tag_name("input").get_attribute("value")
                surname = cells[1].text
                name = cells[2].text
                # address = cells[3].text
                # get list of all the emails from related cell 4
                all_emails = cells[4].text
                # get list of all the phones
                all_phones = cells[5].text
                self.contact_cache.append(User(id=_id, surname=surname, name=name,
                                               all_phones_from_homepage=all_phones,
                                               all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    # additional method; opens edit form
    def get_contacts_info_from_editpage(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        name = driver.find_element_by_name("firstname").get_attribute("value")
        surname = driver.find_element_by_name("lastname").get_attribute("value")
        _id = driver.find_element_by_name("id").get_attribute("value")
        nickname = driver.find_element_by_name("nickname").get_attribute("value")
        company = driver.find_element_by_name("company").get_attribute("value")
        title = driver.find_element_by_name("title").get_attribute("value")
        address = driver.find_element_by_name("address").get_attribute("value")
        # get all the phones from appropriate field
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobile_number = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        address2 = driver.find_element_by_name("address2").get_attribute("value")
        # define param=local variable
        return User(name=name, surname=surname, id=_id, nickname=nickname, company=company, title=title,
                    address=address,
                    homephone=homephone, mobile_number=mobile_number,
                    workphone=workphone, secondaryphone=secondaryphone,
                    address2=address2)

    def get_emails_from_editpage(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        email = driver.find_element_by_name("email").get_attribute("value")
        email2 = driver.find_element_by_name("email2").get_attribute("value")
        email3 = driver.find_element_by_name("email3").get_attribute("value")
        # define param=local variable
        return User(email_1=email, email_2=email2, email_3=email3)  # usr.py

    # additional method; opens contacts on view page
    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contacts_from_viewpage(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        get_text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", get_text).group(1)
        mobile_number = re.search("M: (.*)", get_text).group(1)
        workphone = re.search("W: (.*)", get_text).group(1)
        secondaryphone = re.search("P: (.*)", get_text).group(1)
        return User(homephone=homephone, mobile_number=mobile_number,
                    workphone=workphone, secondaryphone=secondaryphone)

    def get_emails_from_viewpage(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        get_text = driver.find_element_by_id("content").text
        email, email2, email3 = re.findall('\S+@\S+', get_text)
        return User(email_1=email, email_2=email2, email_3=email3)

    def add_cont_to_group(self, contact_id, group_id, group_name):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        driver.find_element_by_name("to_group").click()
        driver.find_element_by_xpath("(//option[@value=%s])[2]" % group_id).click()
        driver.find_element_by_name("add").click()
        driver.find_element_by_link_text('group page "%s"' % group_name)
        self.open_contact_page()

    def remove_cont_from_group(self, contact_id, group_id, group_name):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_element_by_name("group").click()
        driver.find_element_by_xpath("(//option[@value=%s])" % group_id).click()
        self.select_contact_by_id(contact_id)
        driver.find_element_by_css_selector("div:nth-child(9) > input[type=submit]").click()
        driver.find_element_by_link_text('group page "%s"' % group_name)
        self.open_contact_page()

