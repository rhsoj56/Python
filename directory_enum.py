import sys
import requests

sub_list = open("Dirs.txt").read()
dirs = sub_list.splitlines()

for dir in dirs:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory: ", dir_enum)
    