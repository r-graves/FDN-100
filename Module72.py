import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"
# use requests to get the url
response = requests.get(url)
# get the content from the response
content = response.content
# parse the content with soup
soup = BeautifulSoup(content, 'lxml')


# look at the web page source and find out the container for the information we want
# each crater is stored in a li that has the class 'gallerybox'
# tell soup to get the li gallerybox

gallerybox=[]
for x in soup.find_all('li','gallerybox'):
     gallerybox.append(x)


# crater name and crater diameter are inside a div that has the class 'gallerytext'
# tell soup to get the div gallerytext from div gallerybox
gallerytext=[]
for y in soup.find_all('div','gallerytext'):
     gallerytext.append(y)
print(gallerytext[0])
#print(len(gallerytext))
#print(gallerytext[0])
# crater name the string of an anchor tag that is inside a div that has a class 'gallerytext'
# tell soup to get the anchor tag from div gallerytext
titletext = []
for an in soup.find_all('div','gallerytext'):
     for anb in an.find_all('a'):
          anc = anb.get('title')
          titletext.append(anc)


# crater diameter is the string of a span tag that is inside a div that has class 'gallerytext'
# tell soup to get the span tag from div gallerytext
spantext = []
for a in soup.find_all('div','gallerytext'):
       st = (a.span.string)
       spantext.append(st)

# crater thumbnail is inside of the div that has the class 'thumb'
# tell soup to get the div thumb from div gallerybox
thumbnailtext = []
for a3 in soup.find_all('li','gallerybox'):
         for a4 in a3.find_all('div'):
                  a5 = a4.get('class')
                  if a5 == ['thumb']:
                      thumbnailtext.append(a4)


# crater thumbnail source is the 'src' key inside the 'attrs' dictionary of the img tag from div thumb
# tell soup to get the img tag from div thumb
imgtag = []
for a3 in soup.find_all('li','gallerybox'):
         for a4 in a3.find_all('img'):
                  a5 = a4.get('src')
                  imgtag.append(a5)


#print(imgtag[0])
#store name = diameter or name = thumbnail in a dictionary

store_name =dict(zip(titletext,thumbnailtext))



