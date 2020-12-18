import requests

#data = {}
#data['user_id'] = 1
#rsp = requests.post('http://192.168.1.98080/user/get_by_id', json=data)
#print(rsp.text)

#data = {}
#data['x'] = 7
#rsp = requests.post('http://192.168.1.9:8080/test_send_receive', json=data)
#print(rsp.text)

data = {}
data['CustomerID'] = 1
data['CustomerName'] = 'FTP'
data['ContactName'] = 'anta'
data['Address'] = 'nui thanh'
data['City'] = 'da nang'
data['PostalCode'] = '123456'
data['Country'] = 'Vietnam'
rsp = requests.post('http://192.168.1.9:8080/user/insert', json=data)
print(rsp.text)