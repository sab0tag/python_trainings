from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(groupName="new name"))
    app.group.modify_first_group(Group(groupName="New name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(headerDescr="!!!!!!!updated group description"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(headerDescr="updated group description"))
