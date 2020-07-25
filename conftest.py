import pytest
from fixture.application import Application

fixture = None

# fixture init
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(user="admin", pwd="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(user="admin", pwd="secret")
    return fixture

@pytest.fixture(scope = "session", autouse=True)
def stop_fixt(request):
    # define method to logout and destroy fixture
    def fin():
        fixture.session.logout()
        fixture.destroy()
    # destroy fixture
    request.addfinalizer(fin)
    return fixture
