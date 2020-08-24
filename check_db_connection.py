import pymysql

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
