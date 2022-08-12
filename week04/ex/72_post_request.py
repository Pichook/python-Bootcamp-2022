import requests

url = 'https://fakestoreapi.com'

new_item = {
    "title": "test product",
    "price":"13$",
    "description": "Sunset blue",
    "category": "clothes"
}

req = requests.post(f"{url}/products", json=new_item)
print(req.json())