import requests
import json

url = requests.get('http://challenge-api.luizalabs.com/api/product/?page=1')
url_dic = url.json()

for product in url_dic['products']:
    print(product)