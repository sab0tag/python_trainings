__author__ = "igor petrenko"

from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(groupName="New created name"))
    old_groups_list = db.get_group_list()
    group = random.choice(old_groups_list)
    new_group = Group(groupName="Updated group name")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups_lst = db.get_group_list()

    assert len(old_groups_list) == app.group.count()
    group.groupName = new_group.groupName
    assert old_groups_list == new_groups_lst

    if check_ui:
        assert sorted(new_groups_lst, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


'''
def test_modify_group_header(app):
    old_group_list = app.group.get_group_list()
    app.group.modify_first_group(Group(headerDescr="Updated header description"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_lst)


def test_modify_group_footer(app):
    old_group_list = app.group.get_group_list()
    app.group.modify_first_group(Group(footerDescr="Updated footer description"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_lst)

'''
