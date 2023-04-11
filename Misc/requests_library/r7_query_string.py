import requests


payload = {'key1': 'value1', 'key2': 'value2'}

print("Parameters: ", payload)

r = requests.get("https://www.hackthissite.org/missions/realistic/4/products.php?", params=payload)

print(r.url)




