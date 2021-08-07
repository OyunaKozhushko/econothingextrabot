from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['econothingextra_mongodb']
# client.drop_database('<DBNAME>')

# create collections
db['user_states'].drop()
db['user_data'].drop()

mongo_courses = db['courses']
mongo_courses.drop()

print(db.list_collection_names())

print(client.list_database_names())


query = {"telegram_id": 373085647}
print(db['user_states'].find_one(query))

query = {'name': 'wardrobe'}
print(db['courses'].find_one(query))


