__author__ = "igor petrenko"

from model.usr import User
import random


def test_delete_rand_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(User(name="Jason", surname="Williams"))
    old_contacts_lst = db.get_contact_list()
    contact = random.choice(old_contacts_lst)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts_list = db.get_contact_list()

    assert len(old_contacts_lst) - 1 == len(new_contacts_list)  # сравнение длинны списков после удаления объекта
    old_contacts_lst.remove(contact)
    assert old_contacts_lst == new_contacts_list

    if check_ui:
        assert sorted(new_contacts_list, key=User.id_or_max) == sorted(app.contact.get_contacts_list(), key=User.id_or_max)
