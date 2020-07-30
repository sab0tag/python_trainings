import pytest
from fixture.application import Application


# init global variable
fixture = None


# fixture init
@pytest.fixture
def app(request):
    global fixture  # define global variable inside of the method
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(user="admin", pwd="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    # destroy fixture
    request.addfinalizer(fin)
    return fixture
