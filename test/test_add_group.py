# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    old_group_lst = app.group.get_group_list()
    app.group.create(Group(groupName="New test group name", headerDescr="New test header description",
                           footerDescr="New test footer description"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)


def test_empty_group(app):
    old_group_lst = app.group.get_group_list()
    app.group.create(Group(groupName="", headerDescr="", footerDescr=""))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)


def test_add_new_group_one_param(app):
    old_group_lst = app.group.get_group_list()
    app.group.create(Group(groupName="New group with only name created"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)
