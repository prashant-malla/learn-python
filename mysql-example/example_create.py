import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()
sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

cursor.execute(sql)
print("Table created successfully")