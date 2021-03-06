from flask import Flask, jsonify, request
import os
import BusinessObjects as bo
import DataObjects as do 

app = Flask(__name__)

db_ip = os.getenv("db_ip")
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'northwind'

@app.route("/")
def hello():
   return "hello"
@app.route("/test_insert")
def test_insert():
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1,'DAU xanh','Peter','566 Nui Thanh', 'Da Nang','5000','VietNam')
    s1 = c2.insert(c1)
    return s1

@app.route('/test_send_receive', methods=['POST'])
def test_send_receive():
    x = request.json['x']
    y = x + 1
    result = {}
    result['y'] = y
    return jsonify(result), 200

@app.route('/user/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'], data['CustomerName'], data['ContactName'], data['Address'], data['City'], data['PostalCode'], data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/user/all')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/user/get/<int:customer_id>')
def get_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message':result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/user/update/<int:customer_id>',methods=['PUT'])
def update_user_by_id(customer_id):
    data = request.json
    c = bo.Customer(CustomerID = customer_id, CustomerName=data['CustomerName'], ContactName=data['ContactName'],Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customer(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/user/delete/<int:customer_id>', methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).delete(c)
    return jsonify({'message':result[0]}), result[1]

#orderdetail
    
@app.route('/orderdetail/insert', methods=['POST'])
def orderdetail_insert():
    data = request.json
    c1 = bo.oderDetail(data['OrderDetailID'], data['OrderID'], data['ProductID'], data['Quantity'])
    c2 = do.oderDetail(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/orderdetail/all')
def get_all_orderdetail():
    result = do.oderDetail(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/orderdetail/get/<int:od_id>')
def get_orderdetail_by_id(od_id):
    c = bo.oderDetail(CustomerID=od_id)
    result = do.oderDetail(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message':result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/orderdetail/update/<int:od_id>',methods=['PUT'])
def update_orderdetail_by_id(customer_id):
    data = request.json
    c = bo.oderDetail(CustomerID = od_id, OrderID=data['OrderID'], ProductID=data['ProductID'],Quantity=data['Quantity'])
    result = do.oderDetail(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/orderdetail/delete/<int:od_id>', methods=['DELETE'])
def delete_orderdetail_by_id(od_id):
    c = bo.oderDetail(CustomerID=od_id)
    result = do.oderDetail(ConnectionData).delete(c)
    return jsonify({'message':result[0]}), result[1]

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)