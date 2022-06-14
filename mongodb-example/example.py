import pymongo


myclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.xzgisxs.mongodb.net/test")

# print(myclient.list_database_names())

# to check if database exists on the server
dblist = myclient.list_database_names()

for db in dblist:
    print("The database name is: ", db)  # database exists

# to check collection exists on database
mydb = myclient["mydatabase"]
for collection in mydb.list_collection_names():
    print("The collection name is: ", collection)