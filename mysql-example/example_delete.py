import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()

sql = "DELETE FROM customers WHERE name = 'John'"

cursor.execute(sql)

mydb.commit()

print(cursor.rowcount, "record(s) deleted")