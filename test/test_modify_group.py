from model.group import Group

def test_modify_group_name(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(groupName="New name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group(Group(headerDescr="updated group description"))
    app.session.logout()
