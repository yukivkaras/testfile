#!/usr/bin/python
from flask import Flask, request, render_template
from flask_cors import CORS
import json, os
app = Flask(__name__,static_folder="./templates/static")



@app.route('/find_restuarant', methods=["GET"])
def find_restuarant():
    return render_template('index.html')


@app.route('/find_restuarants', methods=["GET"])
def get_address():
    table = open('./database', 'r', encoding='UTF-8').read()
    table_json = json.loads(table)
    address_all = ""
    for i in table_json["datas"]:
        address = i["restaurant_name"]
        address_all += " " + address
    return address_all


@app.route('/add_new_address', methods=["POST"])  # 添加新地址-餐厅
def add_new_address():
    datas = request.get_json()
    address = datas['address']
    restaurant = datas['restaurant']
    new_data = {"datas": [{
        "address_id": 4,
        "restaurant_id": 3,
        "address_name": address,
        "restaurant_name": restaurant,
        "ate_count": 10,
        "create_time": " 2019/11/14",
        "last_ate_time": ""
    }]
    }
    print(datas)
    print(address)
    print(restaurant)
    new_address = open('./database', 'a', encoding='UTF-8')
    new_address.write(json.dumps(new_data))
    new_address.close()
    return 'good'


if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(debug=True, port=8080)
