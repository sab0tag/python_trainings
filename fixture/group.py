from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/groups.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        driver = self.app.driver
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit action
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit action
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.groupName)
        self.change_field_value("group_header", group.headerDescr)
        self.change_field_value("group_footer", group.footerDescr)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_group(self):
        driver = self.app.driver
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        driver = self.app.driver
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                _id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(groupName=text, id=_id))
        return list(self.group_cache)
