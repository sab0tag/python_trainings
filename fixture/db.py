import pymysql
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          passwd=password,
                                          database=name)

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor: # get the results - fetchall
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), groupName=name, headerDescr=header, footerDescr=footer))
        finally:
            cursor.close()
        return lst

    def destroy(self):
        self.connection.close()
