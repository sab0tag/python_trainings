from model.usr import User


def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list()

    def clean(contact):
        return User(id=contact.id,
                    name=contact.name.strip(), surname=contact.surname.strip(),
                    address=contact.address.strip(), address2=contact.address2.strip(),
                    all_phones_from_homepage=merge_phones_(contact),
                    all_emails_from_homepage=merge_emails_(contact))

    db_list = map(clean, db.get_contact_list())

    # compare the lists
    assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)


def merge_phones_(contact):
    return "\n".join(
        filter(lambda x: x != "",
               filter(lambda x: x is not None, [contact.mobile_number, contact.homephone, contact.workphone])))


def merge_emails_(contact):
    return "\n".join(
        filter(lambda x: x != "",
               filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
