from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL  = os.environ.get("MONGODB_URL")
DBNAME =  os.environ.get("DBNAME")

client = MongoClient(MONGODB_URL)
db = client[DBNAME]

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comment', methods=["POST"] )
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    count = db.myfanbook.count_documents({})
    num = count + 1
    doc = {
        'num' : num,
        'name' : name_receive,
        'comment' : comment_receive,
    }
    db.myfanbook.insert_one(doc)
    return jsonify({'msg' : 'Berhasil Ditambahkan!'})

@app.route('/delete', methods=["POST"] )
def delete():
    num_delete = request.form['num_give']
    db.myfanbook.delete_one({'num' : int (num_delete)})
    return jsonify({'msg' : 'Berhasil Dihapus!'})

@app.route("/comment", methods=["GET"])
def comment_get():
    comments_list = list(db.myfanbook.find({},{'_id':False}))
    return jsonify({'comments':comments_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)



