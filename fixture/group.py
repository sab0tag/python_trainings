class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    # вспомогательный метод для выделения элемента checkbox
    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    # выделен вспомогательный метод для заполнения формы при создании/редактировании группы
    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.groupName)
        self.change_field_value("group_header", group.headerDescr)
        self.change_field_value("group_footer", group.footerDescr)

    def modify_first_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        # fill form with a new data
        # submit
        driver.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit update procedure
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()
