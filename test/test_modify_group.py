from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(groupName="updated Name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(headerDescr="updated header description"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footerDescr="updated footer description"))


def test_modify_group_emptyGroupName(app):
    app.group.modify_first_group(Group(groupName=""))
