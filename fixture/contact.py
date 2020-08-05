from model.usr import User
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/index.php")):
            driver.find_element_by_link_text("home").click()

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
        driver = self.app.driver
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contacts_by_index(index)
        # open modification form by clicking on pencil icon
        driver.find_element_by_xpath('//a[img/@src="icons/pencil.png"]').click()
        self.fill_contact_form(new_contact_data)
        # submit action
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, usr):
        driver = self.app.driver
        self.change_field_value("firstname", usr.name)
        self.change_field_value("lastname", usr.surname)
        self.change_field_value("nickname", usr.nick)
        self.change_field_value("title", usr.titl)
        self.change_field_value("company", usr.company_name)
        self.change_field_value("address", usr.street)
        self.change_field_value("mobile", usr.mobile_number)
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
        driver = self.app.driver
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        self.select_contacts_by_index(index)
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to.alert.accept()
        time.sleep(5)
        driver.find_element_by_link_text("home").click()
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
                _id = element.find_element_by_name("selected[]").get_attribute("id")
                name = element.find_elements_by_tag_name("td")[2].text
                surname = element.find_elements_by_tag_name("td")[1].text
                self.contact_cache.append(User(name=name, surname=surname, id=_id))
        return list(self.contact_cache)
