from pymongo import MongoClient
from bson import json_util
from datetime import datetime
from flask import Flask,request,render_template
import json

app = Flask(__name__)
clint = MongoClient('localhost', 27017)
db = clint['chat']

@app.route("/")
def get_root():
    with open ("templates/index.html", "r") as f:
        return f.read()

@app.route('/chat', methods=['PUT'])
def put_chat():
    print("put_chat",request.args.get('user'),request.args.get('word'))
    db.chat.insert_one({
            'user': request.args.get('user'),
            'word': request.args.get('word'),
            'created_at': datetime.now()
        })
    return "ok"

@app.route('/chat', methods=['GET'])
def get_chat():
    try:
        print("get_chat",list(db.chat.find()))
        return json.loads(json_util.dumps({"chats":list(db.chat.find()) }))
    except Exception as e:
        print("get_chat:err",e)
        return {"chats":[]}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)