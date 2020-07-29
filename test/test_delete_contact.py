from model.usr import User


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Jason"))
    app.contact.delete_contact()
