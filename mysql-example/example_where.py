import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()


# sql = "SELECT * FROM customers"
sql = "SELECT * FROM customers WHERE name = 'John'"
# you can use whild cards in the where clause(%, _)
cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    print(row)