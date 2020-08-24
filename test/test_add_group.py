# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata
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
def test_add_new_group(app, db, json_groups): # db - test func param to work with database
    group = json_groups
    old_group_lst = db.get_group_list()
    app.group.create(group)
    assert len(old_group_lst) + 1 == app.group.count()
    new_group_lst = db.get_group_list()
    old_group_lst.append(group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)
