class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user, pwd):
        driver = self.app.driver
        self.app.open_home_page() # method
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(pwd)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

