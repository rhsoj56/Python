import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("DEHASHED CHECKER")
print(ascii_banner)

#script to check for breached credentials on dehashed, if creds are found then to run against social media checker and then test against those sites

dehashed = "https://api.dehashed.com/search?query=email:"

#enter input either email, username, password, hash etc

queried_input = input("Enter an email: ")

#search that input against dehashed api? (DEHASHED API COSTS MONEY, CURRENTLY HAVE 100 CREDITS TO USE)

search = f"{dehashed}{queried_input}"

print(search)


