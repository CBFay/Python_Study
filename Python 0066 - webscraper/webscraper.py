# Use BeautifulSoup and requests modules to scrape a website.
# Created on 1.13.2018 by CB Fay

from bs4 import BeautifulSoup
import requests

# this returns a response object
# adding the text attribute returns a string
source = requests.get("https://en.wikipedia.org/wiki/C_(programming_language)").text

soup = BeautifulSoup(source, 'lxml')

# this returns a list
paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.text)
    print()
