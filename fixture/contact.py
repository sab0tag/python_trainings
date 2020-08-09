from model.usr import User
import re


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

    def fill_contact_form(self, usr):
        self.change_field_value("firstname", usr.name)
        self.change_field_value("lastname", usr.surname)
        self.change_field_value("nickname", usr.nick)
        self.change_field_value("title", usr.titl)
        self.change_field_value("company", usr.company_name)
        self.change_field_value("address", usr.street)
        self.change_field_value("mobile", usr.mobile_number)
        self.change_field_value("home", usr.homephone)
        self.change_field_value("mobile", usr.mobile_number)
        self.change_field_value("work", usr.workphone)
        self.change_field_value("phone2", usr.secondaryphone)
        self.change_field_value("email", usr.email_1)
        self.change_field_value("email", usr.email_2)
        self.change_field_value("byear", usr.b_year)
        self.change_field_value("address2", usr.street2)

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

    def delete_first_group(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contacts_by_index(index)
        # submit delete procedure
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to.alert.accept()
        driver.find_elements_by_css_selector("div.msgbox")
        self.return_to_home_page()
        # driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def count(self):
        driver = self.app.driver
        self.open_contact_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None
    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contact_page()
            self.contact_cache = []
            for element in driver.find_elements_by_css_selector("tr:nth-child(n+2)"):
                cells = element.find_elements_by_tag_name("td")
                _id = element.find_element_by_name("selected[]").get_attribute("id")
                surname = cells[1].text
                name = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(User(name=name, surname=surname, id=_id,
                                               homephone=all_phones[0], mobile_number=all_phones[1],
                                               workphone=all_phones[2], secondaryphone=all_phones[3]))

        return list(self.contact_cache)

    def get_contacts_info_from_editpage(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        name = driver.find_element_by_name("firstname").get_attribute("value")
        surname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobile_number = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return User(name=name, surname=surname, id=id,
                    homephone=homephone, mobile_number=mobile_number,
                    workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index (self, index):
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

