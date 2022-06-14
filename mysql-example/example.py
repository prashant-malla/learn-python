import mysql.connector

# to connect
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
# print(mydb)

# to create a cursor
mycursor = mydb.cursor()

sql = "SHOW DATABASES" # sql command to show databases
mycursor.execute(sql) # execute the sql command
for i in mycursor:
    print(i)

# sql = "CREATE DATABASE db_python" # sql command to create a database
# mycursor.execute(sql) # execute the sql command
# print("Database created successfully")