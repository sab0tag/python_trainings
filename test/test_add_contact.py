__author__ = "igor petrenko"

# -*- coding: utf-8 -*-
from model.usr import User
import pytest
import random
import string


# gen random testdata
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(name="", surname="", nickname="", title="", company="", address="",
                 mobile_number="", homephone="", workphone="", secondaryphone="",
                 email_1="", email_2="", email_3="", address2="")] + [
               User(name=random_string("name", 10), surname=random_string("surname", 10),
                    nickname=random_string("nickname", 10), title=random_string("title", 10),
                    company=random_string("company", 5), address=random_string("address", 20),
                    mobile_number=random_string("mobile", 10), homephone=random_string("homephone", 10),
                    workphone=random_string("workphone", 10), secondaryphone=random_string("second", 10),
                    email_1=random_string("email", 10), email_2=random_string("email2", 10),
                    email_3=random_string("email3", 10),
                    address2=random_string("address2", 20))
               for i in range(5)
           ]

"""
testdata = [
    User(name=name, surname=surname, nickname=nickname, title=title,
         company=company, address=address,
         homephone=homephone, mobile_number=mobile_number)
    for name in ["", random_string("name", 10)]
    for surname in ["", random_string("surname", 10)]
    for nickname in ["", random_string("nickname", 10)]
    for title in ["", random_string("title", 10)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 10)]
    for homephone in ["", random_string("homephone", 10)]
    for mobile_number in ["", random_string("mobile_number", 10)]
    ]
"""


@pytest.mark.parametrize("contact_", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact_):
    old_contacts_lst = app.contact.get_contacts_list()
    # определить локальную переменную для создания контакты
    # contact_ = User(name="Igor", surname="Petrenko", nickname="L0renzo", title="Mr",
    #                company="Luxoft", address="Lake road",
    #                homephone="123", mobile_number="9887654", workphone="231232", secondaryphone="299737",
    #                email="ksjhdckjbscd@mail.ru", email2="msbdjkbsdb@yandex.ru", email3="ksdjbckjbsdjvc@gmail.com",
    #                address2="Radishcheva str.")
    app.contact.create_contact(contact_)  # вызываем переменную в методе create_contact
    assert len(old_contacts_lst) + 1 == app.contact.count()  # where count() is a hash function
    new_contacts_lst = app.contact.get_contacts_list()
    old_contacts_lst.append(contact_)  # добавление нового контакта в old_contact_lst
    assert sorted(old_contacts_lst, key=User.id_or_max) == sorted(new_contacts_lst, key=User.id_or_max)
