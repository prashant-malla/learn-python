import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python",
)

cursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21") # for single row
# cursor.execute(sql, val)

val = [("Ram", "Godawari 21"), ("Bicky", "Lowstreet 4")] # for multiple rows
cursor.executemany(sql, val)

mydb.commit()
print(cursor.rowcount, "row inserted successfully")