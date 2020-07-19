# -*- coding: utf-8 -*-
import pytest
from usr import User
from application import Application


@pytest.fixture
# fixture init
def app(request):
    fixture = Application()
    # вызов параметра; внутри передается функция, которая будет вызвана для разрушения фикстуры
    request.addfinalizer(fixture.destroy)
    return fixture

    # тестовые методы в качестве параметра будут принимать фикстуру
    # при вызове тестового метода будет передан обьект, созданный функцией app
    #


def test_add_user(app):
    app.login(user="admin", pwd="secret")
    app.add_usr(User(name="Igor", surname="Petrenko", nick="sab0tag", titl="QA Engineer", company_name="Luxoft", street="Mayakovskogo avenue", mobile_number="+380661530460", email_1="sabotag1985@gmail.com",
                     email_2="ihor.petrenko@yahoo.com", b_day="2", b_month="November", b_year="1985", street2="Lenina"))
    app.logout()


def test_add_empty_user(app):
    app.login(user="admin", pwd="secret")
    app.add_usr(User(name="", surname="", nick="", titl="", company_name="", street="", mobile_number="", email_1="",
                     email_2="", b_day="", b_month="", b_year="", street2=""))
    app.logout()
