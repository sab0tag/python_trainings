from model.usr import User

def test_modify_contact(app):
    app.session.login(user="admin", pwd="secret")
    app.contact.add_usr(User(name="John", surname="Dow", nick="ranger", titl="Fireman", company_name="Resque team",
                             street="Willard avenue", mobile_number="+380753727384", email_1="sabotag1985@gmail.com",
                             email_2="ihor.petrenko@yahoo.com", b_day="10", b_month="November", b_year="1964", street2="Lakeroad"))
    app.session.logout()
