from model.usr import User


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Jason"))
    old_contacts_lst = app.contact.get_contacts_list()
    app.contact.delete_contact()
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_lst) - 1 == len(new_contacts_list)
