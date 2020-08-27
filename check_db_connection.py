import pymysql
#from fixture.db import dbfixture_
from fixture.orm import ORMFixture
from model.group import Group

#db = dbfixture_(host="localhost",name="addressbook",user="root",password="")
db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    # get db grouplist
    # contacts = db.get_contact_list()
    # contacts = db.get_group_list()
    # contacts = db.get_contacts_in_group(Group(id="12"))
    contacts = db.get_contacts_not_in_group(Group(id="12"))

    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    pass
    # db.destroy()

"""

config = {
    'host': 'localhost',
    'database': 'addressbook',
    'charset': 'utf8mb4',
    'user': 'root',
    'password': ''
}
cnct = pymysql.connect(**config)
try:
    with cnct.cursor() as cursor:
        sql = "SHOW DATABASES"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            print("Done!")
        except:
            print("Something wrong")
finally:
    cnct.close()
"""
