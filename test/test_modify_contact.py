__author__ = "Igor Petrenko"

from model.usr import User
from random import randrange


def test_modify_rand_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Loice", surname="Armstrong"))
    old_contact = app.contact.get_contacts_list()
    index = randrange(len(old_contact))
    contact = User(name="Jason", surname="Low")
    contact.id = old_contact[index].id  # write an old id value
    contact.surname = old_contact[index].surname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contacts_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=User.id_or_max) == sorted(new_contact, key=User.id_or_max)
