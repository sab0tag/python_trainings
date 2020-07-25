from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def add_usr(self, usr):  # add a new contact
        driver = self.app.driver
        # create a new user
        self.fill_contact_form(usr)
        self.open_main_page()

    def fill_contact_form(self, usr):
        driver = self.app.driver
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

    def edit_contact(self, usr):  # exit existing contacts
        driver = self.app.driver
        self.open_main_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img')
        self.fill_contact_form(usr)

    def delete_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_css_selector("#content > form:nth-child(10) > div:nth-child(8) > input[type=button]")
        self.open_main_page()
