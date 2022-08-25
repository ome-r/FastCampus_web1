import math 
import datetime
import math
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"

mongo = PyMongo(app)

@app.route('/write', methods = ["POST"])
def write() :
    name = request.form.get('name')
    content = request.form.get('content')

    mongo.db['wedding'].insert_one({
        "name" : name,
        "content" : content
    })
    return redirect('/')

@app.route('/')
def index() :
    now = datetime.datetime.now()
    wedding = datetime.datetime(2023, 10, 14, 0, 0, 0 )
    diff = (wedding - now).days

    page = int(request.args.get('page', 1))
    limit = 3
    skip = (page - 1) * limit

    count = mongo.db['wedding'].count_documents({})
    max_page = math.ceil(count / limit)

    pages = range(1, max_page + 1)

    guestbooks = mongo.db['wedding'].find().limit(limit).skip(skip)

    return render_template('index.html', 
    diff=diff, 
    guestbooks=guestbooks,
    pages=pages)

if __name__ == '__main__' :
    app.run(host='0,0,0,0', port='5000')