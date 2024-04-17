import os
from dotenv import load_dotenv
import sys
from datetime import datetime
from bson.objectid import ObjectId
load_dotenv()
MYURI = os.getenv("URI")
MYSERVER = os.getenv("SERVERAPI")
PATH = os.getenv("PATHDATA")
DB = os.getenv("DBNAME")
COLECTION = os.getenv("COLECTIONNAME")

sys.path.insert(1,PATH)
from database import conection
print(sys.path)
client = conection(MYURI,MYSERVER)

todolist = client[DB][COLECTION]


def getallinfo():
    cursor = todolist.find({})
    for doc in cursor:
        print(doc)

def createinfo(todo,start,end,description,remember):
    todolist.insert_one({
            "to-do": todo,
            "start": datetime.strptime(start, "%Y-%m-%d"),
            "end": datetime.strptime(end, "%Y-%m-%d"),
            "description": description,
            "remember": remember,
        })

def deletebyid(id):
    todolist.delete_one({"_id":ObjectId})
