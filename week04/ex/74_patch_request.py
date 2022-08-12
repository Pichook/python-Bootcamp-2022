import requests

url= 'https://fakestoreapi.com'

update = {
    "description": "orange"
}

ans = requests.patch(f"{url}/products/21", json=update)
print(ans.json())