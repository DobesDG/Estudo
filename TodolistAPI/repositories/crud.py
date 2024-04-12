import os
from dotenv import load_dotenv
import sys
load_dotenv()
MYURI = os.getenv("URI")
MYSERVER = os.getenv("SERVERAPI")
PATH = os.getenv("PATHFILE")
DB = os.getenv("DBNAME")
COLECTION = os.getenv("COLECTIONNAME")

sys.path.insert(1,PATH)
from database import conection

client = conection(MYURI,MYSERVER)

todolist = client[DB][COLECTION]

print(todolist.find_one({}))