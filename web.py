import requests
from bs4 import BeautifulSoup

inurl = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(url)


soup = BeautifulSoup(page.text,'html')
print(soup)
