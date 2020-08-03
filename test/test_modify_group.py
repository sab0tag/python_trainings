from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="New created name"))
    old_group_list = app.group.get_group_list()
    group = Group(groupName="Updated group name")
    group.id = old_group_list[0].id
    app.group.modify_first_group(group)
    new_group_lst = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_lst)
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)


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
