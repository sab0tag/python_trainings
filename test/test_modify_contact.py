from model.usr import User


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_contact(User(name="Darren"))
    app.contact.modify_contact(User(name="Jason"))


def test_modify_contact_phone_number(app):
    app.contact.modify_contact(User(mobile_number="+380661234567"))


def test_modify_contact_email(app):
    app.contact.modify_contact(User(email_1="test@mail.ru"))


def test_modify_contact_addres(app):
    app.contact.modify_contact(User(street="Willshare avenue 23, appart.12"))
