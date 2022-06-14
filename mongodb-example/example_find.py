import pymongo

# we can use the find and find_one methods to find data in the collection. just like select statement in SQL

mongoclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.xzgisxs.mongodb.net/test")

db = mongoclient["mydatabase"]

collection = db["users"]

# row = collection.find_one({"name": "Alex"})
# print(row)
# doc = collection.find()

doc = collection.find().sort("name", -1) #sort by name 1 and -1 is used to sort in ascending and descending order

# doc = collection.find().limit(2) #limit is used to limit the number of documents to be returned

for row in doc:
    print("{} age is {}".format(row["name"], row["age"]))