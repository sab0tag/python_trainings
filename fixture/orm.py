from pony.orm import *
from datetime import datetime
from model.group import Group
from model.usr import User


# from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):  # where db.Entity class to bind ORMGroup object to db
        # table properties
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, passwd=password)  # conv=decoders)
        self.db.generate_mapping()  # class to match class properties with db table fields
        sql_debug(True)

    def cnvrt_groupsToModel(self, groups):
        def convert(group):
            return Group(id=str(group.id), groupName=group.name, headerDescr=group.header, footerDescr=group.footer)
        return list(map(convert, groups))

    # get objects list
    @db_session
    def get_group_list(self):
        return self.cnvrt_groupsToModel(select(g for g in ORMFixture.ORMGroup))

    def cnvrt_contactsToModel(self, contacts):
        def convert(contact):
            return User(id=str(contact.id), name=contact.firstname, surname=contact.lastname)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        # with db_session: # code should be executed during the session
        return self.cnvrt_contactsToModel(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_orm_object(group)
        return self.cnvrt_contactsToModel(orm_group.contacts)


    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_orm_object(group)
        return self.cnvrt_contactsToModel(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    def get_orm_object(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return orm_group
