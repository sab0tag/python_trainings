# -*- coding: utf-8 -*-
from model.usr import User


def test_add_user(app):
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.create_contact(
        User(name="Igor", surname="Petrenko", nick="sab0tag", titl="QA Engineer", company_name="Luxoft",
             street="Mayakovskogo avenue", mobile_number="+380661530460", email_1="sabotag1985@gmail.com",
             email_2="ihor.petrenko@yahoo.com", b_day="2", b_month="November", b_year="1985", street2="Lenina"))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) + 1 == len(new_contacts_list)

# def test_add_empty_user(app):
#    old_contacts_lst = app.contact.get_contacts_list()
#    app.contact.create_contact(User(name="", surname=""))
#    new_contacts_list = app.contact.get_contacts_list()
#    assert len(old_contacts_lst) + 1 == len(new_contacts_list)
