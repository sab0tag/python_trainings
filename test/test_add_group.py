# -*- coding: utf-8 -*-
from model.group import Group
# import pytest
# from data.groups import constant as testdata

"""
testdata = Group(groupName=name, headerDescr=header, footerDescr=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
    ]
"""


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_new_group(app, db, json_groups, check_ui): # db - test func param to work with database
    group = json_groups
    old_group_lst = db.get_group_list()
    app.group.create(group)
    new_group_lst = db.get_group_list()
    old_group_lst.append(group)
    # assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)

    assert old_group_lst == new_group_lst

    if check_ui:
        assert sorted(new_group_lst, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
