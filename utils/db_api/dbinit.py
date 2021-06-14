from dbconfig import courses
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['dbbot']
# client.drop_database('<DBNAME>')

# create collections
mongo_users = db['users']
mongo_courses = db['courses']

# mongo_users.drop()
#
# # insert info into mongo_courses
# mongo_courses.drop()
# mongo_courses.insert_many(courses)

print(db.list_collection_names())

print(client.list_database_names())


query = {"telegram_id": 373085647}
print(mongo_users.find_one(query))


