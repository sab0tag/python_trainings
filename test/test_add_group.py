# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(groupName="New test group name", headerDescr="New test header description",
                           footerDescr="New test footer description"))


def test_empty_group(app):
    app.group.create(Group(groupName="", headerDescr="", footerDescr=""))


def test_add_new_group_one_param(app):
    app.group.create(Group(groupName="New group with only name created"))
