from model.usr import User
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(User(name="Jason", surname="Wall"))
    # get rand contact
    contacts_lst = orm.get_contact_list()
    contact = random.choice(contacts_lst)
    group_has_contact = orm.groups_has_contact(contact)
    if not group_has_contact:
        groups = orm.get_group_list()
        group_ = random.choice(groups)
        app.contact.add_cont_to_group(contact.id, group_.id, group_.name)
    else:
        group_ = random.choice(group_has_contact)
    # rmv contact to group
    app.contact.remove_cont_from_group(contact.id, group_.id, group_.groupName)
    cont_not_in_group = orm.contacts_not_in_group(group_)
    assert contact in cont_not_in_group
