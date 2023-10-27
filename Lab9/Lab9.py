import json
import requests

r = requests.get('http://127.0.0.1:3000') 
data=r.json()

for widget in data:
    name = widget['name']
    color = widget['color']
    print(f"{name} is {color}")