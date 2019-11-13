#!/usr/bin/python
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def hello_world():
    tiantian = open('./kaixin.txt','r',encoding='UTF-8')
    return tiantian.read()

@app.route('/a',methods=["POST"])
def a():
    name = request.get_json()
    print(name)
    kaixin = open('./kaixin.txt','w',encoding='UTF-8')
    kaixin.write(name)
    kaixin.close()
    return name

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(debug=True,host="192.168.2.107",port=8080)