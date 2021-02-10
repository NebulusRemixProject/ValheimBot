import requests
from bs4 import BeautifulSoup

def get_link(query):
  response = requests.get('https://valheim.fandom.com/wiki/Special:Search?query=' + query)
  soup = BeautifulSoup(response.content, 'html.parser')

  a = soup.find('li', {"class": "unified-search__result"}).find('a')
  if a is None:
    return (None, None)
  return (a['data-title'], a['href'])
