__author__ = "Igor Petrenko"

from model.usr import User


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Darren"))
    old_contacts_lst = app.contact.get_contacts_list()
    contact = User(name="Jason")
    contact.id = old_contacts_lst[0].id # write an old id value
    app.contact.modify_contact(contact)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) == len(new_contacts_list)
    old_contacts_lst[0] = contact
    assert sorted(old_contacts_lst, key=User.id_or_max) == sorted(new_contacts_list, key=User.id_or_max)


'''
def test_modify_contact_phone_number(app):
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.modify_contact(User(mobile_number="+380661234567"))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) == len(new_contacts_list)


def test_modify_contact_email(app):
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.modify_contact(User(email_1="test@mail.ru"))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) == len(new_contacts_list)


def test_modify_contact_addres(app):
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.modify_contact(User(street="Willshare avenue 23, appart.12"))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) == len(new_contacts_list)

'''
