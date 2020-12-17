from flask import Flask
import os
import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)

dp_ip = os.getenv("dp_ip")
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(dp_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'postgres'

@app.route('/')
def.hello():
    c1 = bo.Customer(1, 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
    return c1.CustomerName
@app.router('/test_insert')
def test_insert():
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1, 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
    s1 = c2.insert(c1)
    return s1
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)