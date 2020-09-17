import json
import os.path
from fixture.application import Application
from fixture.db import dbfixture_
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        webconfig = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=webconfig['baseUrl'])  # constructor application
        self.fixture.session.ensure_login(user=webconfig['username'], pwd=webconfig['password'])
        dbconfig = self.target['db']
        self.dbfixture = dbfixture_(host=dbconfig['host'], name=dbconfig['name'], user=dbconfig['user'],
                                    password=dbconfig['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def new_group(self, groupName, headerDescr, footerDescr):
        return Group(groupName=groupName, headerDescr=headerDescr, footerDescr=footerDescr)

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, lst1, lst2):
        assert sorted(lst1, key=Group.id_or_max) == sorted(lst2, key=Group.id_or_max)
