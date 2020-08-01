from model.group import Group


def test_modify_group_name(app):
    check_if_not_empty(app)
    old_group_lst = app.group.get_group_list()
    app.group.modify_first_group(Group(groupName="Updated group name"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) == len(new_group_lst)


def test_modify_group_header(app):
    check_if_not_empty(app)
    old_group_lst = app.group.get_group_list()
    app.group.modify_first_group(Group(headerDescr="Updated header description"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) == len(new_group_lst)


def test_modify_group_footer(app):
    check_if_not_empty(app)
    old_group_lst = app.group.get_group_list()
    app.group.modify_first_group(Group(footerDescr="Updated footer description"))
    new_group_lst = app.group.get_group_list()
    assert len(old_group_lst) == len(new_group_lst)


def check_if_not_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="New created name"))
