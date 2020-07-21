from model.group import Group

def test_modify_first_group(app):
    app.session.login(user="admin", pwd="secret")
    app.group.modify_first_group((Group(groupName="updated Name", headerDescr="updated header description", footerDescr="uopdated footer description")))
    app.session.logout()
