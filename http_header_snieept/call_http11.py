import requests

r = requests.get(url="http://127.0.0.1:8000/http11")
print(r.content)