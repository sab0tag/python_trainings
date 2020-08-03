from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="test"))
    old_group_lst = app.group.get_group_list()
    app.group.delete_first_group()
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) - 1 == len(new_group_lst)
    old_group_lst[0:1] = []
    assert old_group_lst == new_group_lst

