import requests

url = 'https://fakestoreapi.com'

ans = requests.delete(f"{url}/products/21")
print(ans.json())