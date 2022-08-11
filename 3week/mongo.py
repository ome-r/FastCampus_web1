from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local
collection = db.fastcampus

collection.insert_one({
    "title": "FastCampus Course!",
    "content" : "3 Week Course"
})

rows = collection.find()
for row in rows:
     print(row)

row = collection.find_one({'title' : "FastCampus Course!"})
print(row)