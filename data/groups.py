from model.group import Group
# import random
# import string

# setup static test data
testdata = [
    Group(groupName="name1", headerDescr="header1", footerDescr="footer1"),
    Group(groupName="name2", headerDescr="header2", footerDescr="footer2")
]

# gen random testdata
# def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + " " * 10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [Group(groupName="", headerDescr="", footerDescr="")] + [
#    Group(groupName=random_string("name", 10), headerDescr=random_string("header", 20),
#          footerDescr=random_string("footer", 20))
#    for i in range(5)
#]
