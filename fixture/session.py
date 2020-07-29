class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user, pwd):
        driver = self.app.driver
        self.app.open_home_page()  # method
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(pwd)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, user, pwd):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user, pwd)

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[@id='top']/form/b").text == "("+user+")"
