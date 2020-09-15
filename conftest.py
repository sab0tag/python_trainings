import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

# init global variable
fixture = None
target = None


def loadconfig(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


# fixture init
@pytest.fixture
def app(request):
    global fixture  # define global variable inside of the method
    browser = request.config.getoption("--browser")
    webconfig = loadconfig(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=webconfig['baseUrl'])  # constructor application
    fixture.session.ensure_login(user=webconfig['username'], pwd=webconfig['password'])
    return fixture


@pytest.fixture(scope="session")
def db(request):  # request stores the options information during test run
    dbconfig = loadconfig(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=dbconfig['host'],
                          name=dbconfig['name'],
                          user=dbconfig['user'],
                          password=dbconfig['password'])

    def fin():
        dbfixture.destroy

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session")
def orm(request):
    dbconfig = loadconfig(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=dbconfig['host'],
                            name=dbconfig['name'],
                            user=dbconfig['user'],
                            password=dbconfig['password'])
    return ormfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    # destroy fixture
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# add additional parameters inside of function; called once at the beginning ot the test run
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")  # where action will be automatically true if flag is present;


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            # fixture - all the fixture-params starts with data_, testdata - fixture values
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            # fixture - all the fixture-params starts with data_, testdata - fixture values
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
