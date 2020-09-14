from pytest_bdd import given, when, then
from model.usr import User
import random

"""
Create contact
"""
@given('a contact list',
       target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <name>, <surname>, <title>, <company>, <address>, '
       '<mobile_number>, <homephone>, <workphone>, <secondaryphone>, <email_1>, <email_2>, <email_3>, <address2>',
       target_fixture="new_contact")
def new_contact(name, surname, title, company, address, address2, mobile_number, homephone, workphone, secondaryphone,
                email_1, email_2, email_3):
    return User(name=name, surname=surname, title=title, company=company, address=address, address2=address2,
                mobile_number=mobile_number, homephone=homephone, workphone=workphone, secondaryphone=secondaryphone,
                email_1=email_1, email_2=email_2, email_3=email_3)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create_contact(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts_lst = contact_list
    new_contacts_lst = db.get_contact_list()
    old_contacts_lst.append(new_contact)
    assert sorted(old_contacts_lst, key=User.id_or_max) == sorted(new_contacts_lst, key=User.id_or_max)


"""
Delete contact
"""
@given('a contact list with the contacts', target_fixture="exist_contacts_list")
def non_empty_contact_lst(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(User("created contact"))
    return db.get_contact_list()


@given('a random contact from the list',
       target_fixture="rand_contact")
def rand_contact(exist_contacts_list):
    return random.choice(exist_contacts_list)


@when('I delete the contact from the list')
def delete_contact(app, rand_contact):
    app.contact.delete_contact_by_id(rand_contact.id)


@then('the new contact list is equal to the old list with no removed contact')
def verify_contact_deleted(app, db, check_ui, exist_contacts_list, rand_contact):
    old_contacts = exist_contacts_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(rand_contact)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=User.id_or_max) == sorted(app.contact.get_contact_list(), key=User.id_or_max)


"""
    Modify contact
"""
@given('a contact with the data', target_fixture="get_contact")
def get_contact(db):
    return User(name="name", surname="surname")


@when('I enter new contact data')
def edit_contact(app, rand_contact, get_contact):
    app.contact.modify_contact_by_id(rand_contact.id, get_contact)


@then('the new contact list is equal to the old list with the edited contact')
def verify_contact_modified(app, db, check_ui, exist_contacts_list, rand_contact, get_contact):
    old_contacts = exist_contacts_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    rand_contact.name = get_contact.name
    # assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=User.id_or_max) == sorted(app.contact.get_contact_list(), key=User.id_or_max)
