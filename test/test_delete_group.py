__author__ = "igor petrenko"

from model.group import Group
from random import randrange


def test_delete_rand_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="test"))
    old_group_lst = app.group.get_group_list()
    index = randrange(len(old_group_lst))
    app.group.delete_group_by_index(index)
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) - 1 == len(new_group_lst)
    old_group_lst[index:index + 1] = []
    assert old_group_lst == new_group_lst
