import requests

def status_code_checker(url):
    res = requests.get(url)
    print(f"The status code of {url} is {res.status_code}")


try:
    status_code_checker(input("Enter website URL in https://www.name.com format: "))
except:
    print("An error has occured, please try again.")