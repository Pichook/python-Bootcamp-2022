import requests

url = 'https://fakestoreapi.com'

update = {
    "title": "updated_item",
    "price": "15$",
    "description": "Peach orange"
}

ans = requests.put(f"{url}/products/21", json=update)
print(ans.json())