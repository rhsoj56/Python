import requests

url = 'https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg'

r = requests.get(url, allow_redirects=True)

open('cute-cat-photos-1593441022.jpg', 'wb').write(r.content)