import pytest
from fixture.application import Application
import master

# init global variable
fixture = None


# fixture init
@pytest.fixture
def app(request):
    global fixture  # define global variable inside of the method
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url) # constructor application
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(user=master.usr, pwd=master.pwd)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    # destroy fixture
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost:8080/addressbook/")
