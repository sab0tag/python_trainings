__author__ = "igor petrenko"

# -*- coding: utf-8 -*-
from model.usr import User


def test_add_user(app):
    old_contacts_lst = app.contact.get_contacts_list()
    # определить локальную переменную для создания контакты
    contact_ = User(name="Igor", surname="Petrenko")
    app.contact.create_contact(contact_)  # вызываем переменную в методе create_contact
    assert len(old_contacts_lst) + 1 == app.contact.count()  # where count() is a hash function
    new_contacts_lst = app.contact.get_contacts_list()
    old_contacts_lst.append(contact_)  # добавление нового контакта в old_contact_lst
    assert sorted(old_contacts_lst, key=User.id_or_max) == sorted(new_contacts_lst, key=User.id_or_max)
