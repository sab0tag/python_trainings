import pytest
from fixture.application import Application
import json
import os.path

# init global variable
fixture = None
target = None


# fixture init
@pytest.fixture
def app(request):
    global fixture  # define global variable inside of the method
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # get the current directory for file
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])  # constructor application
    fixture.session.ensure_login(user=target['username'], pwd=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    # destroy fixture
    request.addfinalizer(fin)
    return fixture


# add additional parameters inside of function; called once at the beginning ot the test run
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
