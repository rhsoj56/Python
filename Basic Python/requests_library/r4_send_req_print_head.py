import requests

r = requests.get("https://www.google.com")
response = r.headers
print(response)

print("Date: ", r.headers['date'])
print("Content-Type: ", r.headers['content-type'])