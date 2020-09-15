from pytest_bdd import given, when, then
from model.group import Group


@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()


@given('a group with <groupName>, <headerDescr> and <footerDescr>', target_fixture="new_group")
def new_group(groupName, headerDescr, footerDescr):
    return Group(groupName=groupName, headerDescr=headerDescr, footerDescr=footerDescr)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_group_lst = group_list
    new_group_lst = db.get_group_list()
    old_group_lst.append(new_group)
    assert sorted(old_group_lst, key=Group.id_or_max) == sorted(new_group_lst, key=Group.id_or_max)
