# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    old_group_lst = app.group.get_group_list()
    # определить локальную переменную для создания группы
    group = Group(groupName="New test group name", headerDescr="New test header description",
                  footerDescr="New test footer description")
    app.group.create(group)
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)
    old_group_lst.append(group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)


def test_empty_group(app):
    old_group_lst = app.group.get_group_list()
    group = (Group(groupName="", headerDescr="", footerDescr=""))
    app.group.create(group)
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)
    old_group_lst.append(group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)


def test_add_new_group_one_param(app):
    old_group_lst = app.group.get_group_list()
    group = (Group(groupName="New group with only name created"))  # локальная переменная, которая содержит группу
    app.group.create(group)  # переменная передается в метод create
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) + 1 == len(new_group_lst)
    old_group_lst.append(group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)
