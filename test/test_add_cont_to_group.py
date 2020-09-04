from model.usr import User
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if orm.get_contact_list() == 0:
        app.contact.create_contact(User(name="Jason", surname="Wall"))
    # get random contact
    contacts_lst = orm.get_contact_list()
    contact = random.choice(contacts_lst)
    group_hasnt_contact = orm.groups_hasnt_contact(contact)
    if not group_hasnt_contact:
        group = Group(groupName="TestGroup")
        app.group.create(group)
    else:
        group = random.choice(group_hasnt_contact)
    # add contact to group
    app.contact.add_cont_to_group(contact.id, group.id, group.groupName)
    cont_in_group = orm.contacts_in_group(group)
    assert contact in cont_in_group
