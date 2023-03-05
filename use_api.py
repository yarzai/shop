import requests

res = requests.get("http://localhost:8000/api/products/products/")
data = res.json()
print(data[0]['title'])
