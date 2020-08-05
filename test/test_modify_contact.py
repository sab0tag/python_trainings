__author__ = "Igor Petrenko"

from model.usr import User
from random import randrange


def test_modify_rand_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="New created user"))
    old_contact = app.contact.get_contacts_list()
    index = randrange(len(old_contact))
    contact = User(name="Jason")
    contact.id = old_contact[index].id  # write an old id value
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=User.id_or_max) == sorted(new_contact, key=User.id_or_max)


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


def test_modify_contact_address(app):
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.modify_contact(User(street="Wiltshire avenue 23, apart.12"))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) == len(new_contacts_list)

'''
