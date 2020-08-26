import pymysql
from fixture.db import dbfixture_

db = dbfixture_(host="localhost",
                name="addressbook",
                user="root",
                password="")
try:
    # get db grouplist
    # grps = db.get_group_list()
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()

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
