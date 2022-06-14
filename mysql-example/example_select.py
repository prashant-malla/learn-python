import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

result = cursor.fetchall()
for row in result:
    print(row)
    