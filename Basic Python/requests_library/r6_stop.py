import requests

print("timeout = 0.001")

try:
    r = requests.get("https://www.google.com", timeout = 0.001)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)

print("\ntimeout = 1.0")

try:
    r = requests.get("https://www.google.com", timeout = 1.0)
    print("Connected...")
except requests.exceptions.RequestException as e:
    print(e)


