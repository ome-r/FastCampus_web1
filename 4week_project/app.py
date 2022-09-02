# from fileinput import filename
import os
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect
from flask.json import jsonify 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"

mongo = PyMongo(app)

@app.route('/dang')
def dang() :
    product_s = mongo.db.product
    product = product_s.find_one({"title" : request.args.get('title')})

    return jsonify({
        'tltle' : product.get('title'),
        'content' : product.get('content')
    })
    
@app.route('/writepage')
def writepage():
    return render_template('write.html')


@app.route('/write', methods=['POST'])
def write():

    fileinfo = request.files['image']
    filepath = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filepath, 'static')
   
    fileinfo.save(os.path.join(filepath, fileinfo.filename))

    product_s = mongo.db.product

    product_s.insert_one({
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'price': request.form.get('price'),
        'location': request.form.get('location'),
        'image': fileinfo.filename
    })

    return redirect('/')

@app.route('/')
def main() :
    product_s = mongo.db.product
    products = product_s.find()
    return render_template('1list.html' , products=products)

    return redirect('/')

if __name__ == '__main__' :
    app.run()