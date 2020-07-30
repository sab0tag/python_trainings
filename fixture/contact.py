class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/index.php") and len(driver.find_elements_by_name("user")) > 0):
            driver.find_element_by_link_text("home").click()

    def create_contact(self, usr):  # add a new contact
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(usr)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contact_page()

    def modify_contact(self, new_contact_data):
        driver = self.app.driver
        self.select_first_contact()
        driver.find_element_by_xpath('//a[img/@src="icons/pencil.png"]').click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name("update").click()
        self.open_contact_page()

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

    def delete_contact(self):
        driver = self.app.driver
        self.select_first_contact()
        driver.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]")
        self.open_contact_page()

    def count(self):
        driver = self.app.driver
        self.open_contact_page()
        return len(driver.find_elements_by_name("selected[]"))

