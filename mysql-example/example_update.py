import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE name = %s"
val = ("Valley 345", "John")

cursor.execute(sql, val)
mydb.commit()
print(cursor.rowcount, "record(s) updated")
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for row in result:
    print(row)