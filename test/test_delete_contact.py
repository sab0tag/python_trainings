__author__ = "igor petrenko"

from model.usr import User
from random import randrange

def test_delete_rand_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Jason"))
    old_contacts_lst = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_lst))
    app.contact.delete_contact_by_index(index)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) - 1 == len(new_contacts_list) # сравнение длинны списков после удаления объекта
    old_contacts_lst[index:index+1] = []
    assert old_contacts_lst == new_contacts_list
