import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
# use requests to get the url
response = requests.get(url)
# get the content from the response
content = response.content
# parse the content with soup
soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
