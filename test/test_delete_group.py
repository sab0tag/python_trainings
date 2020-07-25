def test_delete_first_group(app):
    app.session.login(user="admin", pwd="secret")
    app.group.delete_group()
    app.session.logout()
