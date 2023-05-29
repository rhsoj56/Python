import requests

send = requests.get('https://www.google.com')
print(send.text) #.text will print all text from get request

print("\n")

print(send.content) #prints content of page

print('\n')

r = requests.get("https://www.microsoft.com", stream = True) #stream=true means only response headers have been downloaded and connection will stay open until we get the .content

print(r.raw) #raw socket response
print(r.raw.read(15))

