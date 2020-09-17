import json
import os.path
from fixture.application import Application
from fixture.db import dbfixture_
from model.group import Group
from model.usr import User


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

    # Groups
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

    ###############
    # Contacts
    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self, name, surname, company, address, mobile_number):
        return User(name=name, surname=surname, company=company, address=address, mobile_number=mobile_number)

    def create_contact(self, contact):
        self.fixture.contact.create_contact(contact)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def modify_contact(self, contact, new_contact):
        self.fixture.contact.modify_contact_by_id(contact.id, new_contact)

    def contact_lists_should_be_equal(self, lst1, lst2):
        assert sorted(lst1, key=User.id_or_max) == sorted(lst2, key=User.id_or_max)
