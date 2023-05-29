import requests

#created as a function this time. couldn't get json_name to work for different inputs so chatgpt suggested putting in the if/else statement

def json_parser(json_name):
    r = requests.get("https://api.github.com")
    response = r.json()
    if json_name in response:
        print(f"{json_name} is", response[json_name])
    else:
        print(f"{json_name} wasn't found")


json_parser('emails_url')
json_parser('followers_url')


