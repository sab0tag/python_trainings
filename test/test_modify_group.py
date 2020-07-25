from model.group import Group


def test_modify_group_name(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(groupName="updated Name"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(headerDescr="updated header description"))
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(footerDescr="updated footer description"))
    app.session.logout()


def test_modify_group_emptyGroupName(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(groupName=""))
    app.session.logout()
