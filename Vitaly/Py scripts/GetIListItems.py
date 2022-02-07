import requests
import json

res = requests.get('http://api.gw2tp.com/1/bulk/items-names.json')

items = json.dumps(res.text)

