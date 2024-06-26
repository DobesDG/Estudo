from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def conection(uri, server):
    client = MongoClient(uri, server_api=ServerApi(server))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client

