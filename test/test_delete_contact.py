def test_delete_contact(app):
    app.session.login(user="admin", pwd="secret")
    app.contact.delete_contact()
    app.session.logout()
