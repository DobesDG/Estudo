from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://douglasgalvao06:74185599@studybase.3hndkwr.mongodb.net/?retryWrites=true&w=majority&appName=studybase"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client["Study"]

todolist = database["To-do-list"]

cursor = todolist.find_one({})

print(cursor)
