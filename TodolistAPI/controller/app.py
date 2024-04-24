from flask import request,Flask, Response, render_template, redirect,url_for
import json
import os
from dotenv import load_dotenv
import sys
load_dotenv()
MYURI = os.getenv("URI")
MYSERVER = os.getenv("SERVERAPI")
PATH = os.getenv("PATHREPO")
PATH2 = os.getenv("PATHTEMP")
DB = os.getenv("DBNAME")
COLECTION = os.getenv("COLECTIONNAME")
sys.path.insert(1,PATH)

from crud import *

app = Flask(__name__, template_folder = 'templates/')
@app.route("/",methods= ["GET","POST"])
def index():
    if request.method == "GET":
        getallinfo()
        all_todos = getallinfo()
        return render_template('home.html', todolist = all_todos)
    if request.method == "POST":
        content = request.form['content']
        description = request.form['description']
        start = request.form['start']
        end = request.form['end']
        remember = request.form.getlist('degree[]')
        if len(remember) == 0:
            remember = "Never"
        if len(remember) == 7:
            remember = "Always"
        createinfo(content,start,end,description,remember)
        all_todos = todolist.find()
        return render_template('home.html', todolist = all_todos)
    
@app.route("/<id>/delete/", methods = ["POST"])
def delete(id):
    deletebyid(id)
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)
