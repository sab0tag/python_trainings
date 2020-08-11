__author__ = "igor petrenko"

import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contacts_list()[0] # read and get contacts info from the homepage
    contact_from_editpage = app.contact.get_contacts_info_from_editpage(0)  # get contacts info from the editpage
    # compare all the phones from homepage and edit page
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_editpage)
    # assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_editpage)
    assert contact_from_homepage.email == contact_from_editpage.email
    assert contact_from_homepage.email2 == contact_from_editpage.email2
    assert contact_from_homepage.email3 == contact_from_editpage.email3


def test_phones_on_contacts_viewpage(app):
    contact_info_from_viewpage = app.contact.get_contacts_from_viewpage(0)
    contact_info_from_editpage = app.contact.get_contacts_info_from_editpage(0)
    assert contact_info_from_viewpage.homephone == contact_info_from_editpage.homephone
    assert contact_info_from_viewpage.workphone == contact_info_from_editpage.workphone
    assert contact_info_from_viewpage.mobile_number == contact_info_from_editpage.mobile_number
    assert contact_info_from_viewpage.secondaryphone == contact_info_from_editpage.secondaryphone
    # assert contact_info_from_viewpage.email == contact_info_from_editpage.email
    # assert contact_info_from_viewpage.email2 == contact_info_from_editpage.email2
    # assert contact_info_from_viewpage.email3 == contact_info_from_editpage.email3


# implement method to clear all the strings from additional symbols
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # merge
                            map(lambda x: clear(x),  # apply clear() func and remove all the spec symbols
                                filter(lambda x: x is not None,  # filter all the values None
                                       [contact.homephone, contact.mobile_number, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(email_):
    return "\n".join(filter(lambda x: x != "",  # merge
                            map(lambda x: clear(x),  # apply clear() func and remove all the spec symbols
                                filter(lambda x: x is None,  # filter all the values None
                                       [email_.email, email_.email2, email_.email3]))))
