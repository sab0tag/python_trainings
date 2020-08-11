# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


# gen random testdata
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(groupName="", headerDescr="", footerDescr="")] + [
    Group(groupName=random_string("name", 10), headerDescr=random_string("header", 20),
          footerDescr=random_string("footer", 20))
    for i in range(5)
]

"""
testdata = Group(groupName=name, headerDescr=header, footerDescr=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
    ]
"""


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_new_group(app, group):
    old_group_lst = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group_lst) + 1 == app.group.count()
    new_group_lst = app.group.get_group_list()
    old_group_lst.append(group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)
