from flask import request,Flask, Response
import json
from crud import todolist

app = Flask(__name__)
@app.route("/to-do-list",methods= ["GET"])
def getlist():
    data = list(todolist.find_one({}))
    return Response(
        response= json.dumps(data),
        status= 500,
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run(port=5000,host="localhost",debug=True)
