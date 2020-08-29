from model.usr import User
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(User(name="Jason", surname="Wall"))
    old_contacts_lst = db.get_contact_list()  # get contact lst from db
    old_groups_lst = db.get_group_list()  # get group list from db
    contact = random.choice(old_contacts_lst)
    group = random.choice(old_groups_lst)
    app.contact.add_cont_to_group(contact.id, group.id, group.groupName)
    cont_in_group = orm.get_contacts_in_group(
        Group(id=group.id, groupName=group.groupName, headerDescr=group.headerDescr, footerDescr=group.footerDescr))
    print(cont_in_group)
    assert contact in cont_in_group
