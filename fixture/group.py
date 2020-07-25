class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # find 1st element in list
        # select checkbox
        # hit "Edit Group" button
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit update procedure
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        driver.find_element_by_name("group_name").send_keys(group.groupName)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.headerDescr)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footerDescr)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()
