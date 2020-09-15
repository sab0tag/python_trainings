__author__ = "Igor Petrenko"

from model.usr import User
import random


def test_modify_rand_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(User(name="Loice", surname="Armstrong", email_1="skjdbkjbskjdbc@test.ru", email_2="sdcljnljsndbcj@ya.ru"))
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    new_contact = User(name="Jason", surname="Low", email_1="ksbdcjkbkjbsdc@ru", email_3="sdncjsbsdkbck@ya.ru")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts_lst = db.get_contact_list()

    assert len(old_contacts_list) == app.contact.count()
    contact.name = new_contact.name
    assert old_contacts_list == new_contacts_lst

    if check_ui:
        assert sorted(new_contacts_lst, key=User.id_or_max) == sorted(app.contact.get_contacts_list(), key=User.id_or_max)
