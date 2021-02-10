import requests
from bs4 import BeautifulSoup

def get_link(query):
  response = requests.get('https://valheim.fandom.com/wiki/Special:Search?query=' + query)
  soup = BeautifulSoup(response.content, 'html.parser')

  li = soup.find('li', {"class": "unified-search__result"})
  if li is None:
    return (None, None)
  a = li.find('a')
  return (a['data-title'], a['href'])