__author__ = "igor petrenko"

import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_editpage = app.contact.get_contacts_info_from_editpage(0)
    assert contact_from_homepage.homephone == clear(contact_from_editpage.homephone)
    assert contact_from_homepage.workphone == clear(contact_from_editpage.workphone)
    assert contact_from_homepage.mobile_number == clear(contact_from_editpage.mobile_number)
    assert contact_from_homepage.secondaryphone == clear(contact_from_editpage.secondaryphone)


def test_phones_on_contacts_viewpage(app):
    contact_from_viewpage = app.contact.get_contacts_from_viewpage(0)
    contact_from_editpage = app.contact.get_contacts_info_from_editpage(0)
    assert contact_from_viewpage.homephone == contact_from_editpage.homephone
    assert contact_from_viewpage.workphone == contact_from_editpage.workphone
    assert contact_from_viewpage.mobile_number == contact_from_editpage.mobile_number
    assert contact_from_viewpage.secondaryphone == contact_from_editpage.secondaryphone


# implement method to clear all the strings from additional symbols
def clear(s):
    return re.sub("[() -]", "", s)
