import pytest
from fixture.application import Application

# fixture init
@pytest.fixture()
def app(request):
    fixture = Application()
    app.session.login(user="admin", pwd="secret")
    # destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture
