from model.usr import User
import random
from model.group import Group


def test_delete_cont_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(User(name="Casey", surname="Neistat"))
    if app.group.count() == 0:
        app.group.create(Group(groupName="testname", headerDescr="header", footerDescr="footer"))
    # get rand contact
    contacts_lst = orm.get_contact_list()
    contact = random.choice(contacts_lst)
    # check if groups has contact chosen randomly
    group_has_contact = orm.groups_has_contact(contact)
    if not group_has_contact:
        groups = orm.get_group_list()
        group = random.choice(groups)
        app.contact.add_cont_to_group(contact.id, group.id, group.name)
    else:
        group = random.choice(group_has_contact)
    # remove contact from group
    app.contact.remove_contact_from_group(group.id, contact.id)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group
