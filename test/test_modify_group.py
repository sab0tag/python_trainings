from model.group import Group


def test_modify_group_name(app):
    check_if_not_empty(app)
    app.group.modify_first_group(Group(groupName="Updated group name"))


def test_modify_group_header(app):
    check_if_not_empty(app)
    app.group.modify_first_group(Group(headerDescr="Updated header description"))


def test_modify_group_footer(app):
    check_if_not_empty(app)
    app.group.modify_first_group(Group(footerDescr="Updated footer description"))


def check_if_not_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="New created name"))
