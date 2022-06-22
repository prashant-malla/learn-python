import pymongo

myclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.xzgisxs.mongodb.net/test")

mydb = myclient["mydatabase"]

mycollection = mydb["users"]

# single_user = {"name": "Alex", "age": "25"}
# mycollection.insert_one(single_user)

multiple_user = [
    {"name": "Claire", "age": "27"},
    {"name": "Peter", "age": "25"},
    {"name": "Amy", "age": "23"},
    {"name": "Hannah", "age": "25"},
    {"name": "Michael", "age": "27"},
    {"name": "Sandy", "age": "23"},
]
mycollection.insert_many(multiple_user)

print("Inserted a document into the collection")
