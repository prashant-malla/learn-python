import pymongo

mongoclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.xzgisxs.mongodb.net/test")

db = mongoclient["mydatabase"]
col = db["users"]

# query = {"age": "27"}
# newQuery = {"$set": {"age": "28"}}
# x = col.update_one(query, newQuery)

query = {"age": "25"}
newQuery = {"$set": {"age": "50"}}
x = col.update_many(query, newQuery)

print(x.modified_count, "document updated")

col.update_one(query, newQuery)
doc = col.find()
for i in doc:
    print(i['name'], i['age'])