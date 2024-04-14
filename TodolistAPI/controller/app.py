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
sys.path.insert(2,PATH2)

from crud import *

app = Flask(__name__, template_folder = PATH2)
@app.route("/",methods= ["GET"])
def get():
    getallinfo()
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
