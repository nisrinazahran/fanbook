from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://test:sparta@ac-rlfmp5k-shard-00-00.waymkxr.mongodb.net:27017,ac-rlfmp5k-shard-00-01.waymkxr.mongodb.net:27017,ac-rlfmp5k-shard-00-02.waymkxr.mongodb.net:27017/?ssl=true&replicaSet=atlas-yzrfcr-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.fanbook

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



