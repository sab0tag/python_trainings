# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(groupName="newGroup", headerDescr="header description", footerDescr="footer description"))

def test_empty_group(app):
    app.group.create(Group(groupName="", headerDescr="", footerDescr=""))
