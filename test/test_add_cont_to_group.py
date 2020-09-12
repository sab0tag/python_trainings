from model.usr import User
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create(User(name="John", surname="Connor"))
    # get rand contact
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    # check if groups hasn't contact chosen randomly
    group_hasnt_contact = orm.groups_hasnt_contact(contact)
    if not group_hasnt_contact:
        group = Group(groupName="add test group")
        app.group.create(group)
    else:
        group = random.choice(group_hasnt_contact)
    # add contact to group
    app.contact.add_cont_to_group(contact.id, group.id, group.groupName)
    # check is contact has been added
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group
