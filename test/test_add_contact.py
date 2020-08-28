__author__ = "igor petrenko"

# -*- coding: utf-8 -*-
from model.usr import User


def test_add_user(app, db, json_contacts, check_ui):
    contact_ = json_contacts
    old_contacts_lst = db.get_contact_list()
    app.contact.create_contact(contact_)  # вызываем переменную в методе create_contact
    new_contacts_lst = db.get_contact_list()
    old_contacts_lst.append(contact_)  # добавление нового контакта в old_contact_lst

    assert sorted(old_contacts_lst, key=User.id_or_max) == sorted(new_contacts_lst, key=User.id_or_max)

    if check_ui:
        assert sorted(new_contacts_lst, key=User.id_or_max) == sorted(app.contact.get_contacts_list(), key=User.id_or_max)
