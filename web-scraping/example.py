import requests
from bs4 import BeautifulSoup
import urllib.request

req = requests.get("https://nabilbank.com/individual")

if req.status_code != 200:
    print('not 200')

# print(req.content)
# print(req.text)

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())
# print(soup.get_text())

# to get all urls
# for  link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.find_all('a'))

# get all images which were available in the page
for image in soup.find_all('img'):
    url = image.get('src')
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)

    print('image successfully downloaded', filename)

# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent.name)