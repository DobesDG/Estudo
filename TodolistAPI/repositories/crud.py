from data.database import client

base = client["Study"]

todolist = base["To-do-list"]

cursor = todolist.find_one({})

print(cursor)