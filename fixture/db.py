import pymysql.cursors
from model.group import Group
from model.usr import User


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          passwd=password,
                                          database=name,
                                          autocommit=True)  # autocommit - reset caching after every request

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:  # get the results - fetchall
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), groupName=name, headerDescr=header, footerDescr=footer))
        finally:
            cursor.close()
        return lst

    # method to get_contacts_list
    def get_contact_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, address2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:  # get the results - fetchall
                (id, firstname, lastname, address, address2) = row
                lst.append(User(id=str(id), name=firstname, surname=lastname, address=address, address2=address2))
        finally:
            cursor.close()
        return lst

    # call destroy method to close connection
    def destroy(self):
        self.connection.close()
