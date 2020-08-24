__author__ = "igor petrenko"

from model.group import Group
from random import randrange
import random


def test_delete_rand_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(groupName="test"))
    old_group_lst = db.get_group_list()
    group = random.choice(old_group_lst)
    index = randrange(len(old_group_lst))
    app.group.delete_group_by_id(group.id)
    # since items in the database and user interface are sorted according to different rules, we select data by ID (implemented two new test methods: select by id, delete by id)
    new_group_lst = db.get_group_list()
    assert len(old_group_lst) - 1 == len(new_group_lst)
    old_group_lst.remove(group)
    assert old_group_lst == new_group_lst
