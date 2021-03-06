from model.group import Group
from timeit import timeit


# send as a params two fixtures; where app - access to the user ui via browser, db - grant access to db
def test_group_list(app, db):
    # match the results
    ui_list = app.group.get_group_list()

    # implement func to clear the spaces inside of db_list object
    def clean(group):
        return Group(id=group.id, groupName=group.groupName.strip())

    db_list = map(clean, db.get_group_list())

    # compare the lists
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


"""
from model.group import Group
from timeit import timeit

# send as a params two fixtures; where app - access to the user ui via browser, db - grant access to db
def test_group_list(app, db):
    # match the results
    print(timeit(lambda: app.group.get_group_list(), number=1))
    
    # implement func to clear the spaces inside of db_list
    def clean(group):
        return Group(id=group.id, groupName=group.groupName.strip())

    print(timeit(lambda: map(clean, db.get_group_list(), number=1000)))

    # compare the lists
    assert False

"""
