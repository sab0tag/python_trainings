# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


# fixture init
@pytest.fixture()
def app(request):
    fixture = Application()
    # destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(user="admin", pwd="secret")
    app.group.create(Group(groupName="newGroup", headerDescr="header description", footerDescr="footer description"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(user="admin", pwd="secret")
    app.group.create(Group(groupName="", headerDescr="", footerDescr=""))
    app.session.logout()
