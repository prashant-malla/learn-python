import pymongo

mongoclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.xzgisxs.mongodb.net/test")

db = mongoclient["mydatabase"]
col = db["users"]

# delete_one() method detele one document from the collection
# delete_many() method detele many documents from the collection

# query = {"name": "Alex"}
# success = col.delete_one(query)
# print(success.deleted_count, "document deleted")

query = {"age": "27"}
success = col.delete_many(query)

print(success.deleted_count, "document deleted")

doc = col.find()
for row in doc:
    print(row['name'], row['age'])