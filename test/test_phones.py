__author__ = "igor petrenko"


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_editpage = app.contact.get_contacts_info_from_editpage(0)
    assert contact_from_homepage.homephone == contact_from_editpage.homephone
    assert contact_from_homepage.workphone == contact_from_editpage.workphone
    assert contact_from_homepage.mobile_number == contact_from_editpage.mobile_number
    assert contact_from_homepage.secondaryphone == contact_from_editpage.secondaryphone

