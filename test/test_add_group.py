# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(groupName="newGroup", headerDescr="header description", footerDescr="footer description"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(user="admin", pwd="secret")
    app.group.create(Group(groupName="", headerDescr="", footerDescr=""))
    app.session.logout()
