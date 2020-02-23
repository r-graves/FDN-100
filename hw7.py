"""Homework 7 will look at a wikipedia page based on cratters of the moon or cities in canada. From there, the
get tags function will find all the occurances ofthe specified tag and return 'usefull' information pretaining to that tag"""
import requests
from bs4 import BeautifulSoup

#get the website coming in
def get_url():
    url = input("Please specify a URL: ")
    #url = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
    #url = 'https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon'
    return(url)
#get the tags coming in
def tag_ui():
    tags_in = input("Please specify what tag you are looking for: ")
    #tags_in = 'table'
    return(tags_in)

#get_tags does the heavy lifting, using soup to drill down to the tag we are looking for
def get_tags(soup,tag):
    tag_back = []
    if tag == 'div':
       tag_out = 0
       for x in soup.find_all('div'):
           tag_out = tag_out + 1
       tag_out2 = str('There are ' + str(tag_out) + ' div on the page')
       tag_back.append(tag_out2)
    #for the list tag I will count the number of divs
    elif tag == 'li':
       tag_out = 0
       for x in soup.find_all(tag):
           for y in x.find_all('div'):
               tag_out = tag_out + 1
       tag_out2 = str('There are ' + str(tag_out) + ' div on the page')
       tag_back.append(tag_out2)
    #get all the links referenced in anchor tags
    elif tag == 'a':
       for x in soup.find_all(tag):
           y = str(x.get('href'))
           if str(y[0:4]) == 'http':
               tag_back.append(y)
    #get all tiltles nexted within 'P' tags
    elif tag == 'p':
        for x in soup.find_all(tag):
            for y in x.find_all('a'):
               z = y.get('title')
               tag_back.append(z)
    #get the location, height, and width for img tags
    elif tag == 'img':
        for x in soup.find_all(tag):
            src = x.get('src')
            width = x.get('width')
            height = x.get('height')
            tag_out = str("Image at " + str(src) + ' has dimensions of ' + str(width) + ' by ' + str(height))
            tag_back.append(tag_out)
    #get a list of all the cities in canada
    elif tag == 'table':
        for x in soup.find_all(tag):
            x1 = x.get('class')
            if x1 == ['wikitable', 'sortable']:
                for x2 in x.find_all('tbody'):
                    for x3 in x2.find_all('a'):
                        x4 = x3.get('title')
                        x5 = str(x4)
                        comma_ct = x5.count(',')
                        if comma_ct == 0 and x4 is not None:
                            x5 = str(x4 + ' is a city in Canada')
                            tag_back.append(x5)
    return tag_back

#create an output file
def write_out(tag_back):
    fout = open('hw7_out.txt', 'w')
    for x in tag_back:
        y = str(x + '\n')
        fout.write(y)
    fout.close()

#main funciton controls everything
def main():
    url = get_url()
    tags_in = tag_ui()
    # use requests to get the url
    response = requests.get(url)
    # get the content from the response
    content = response.content
    # parse the content with soup, send to get_tags
    tag_back = get_tags(BeautifulSoup(content, 'lxml'),tags_in)
    #write the output to a text file
    write_out(tag_back)


#below runs the program
if __name__ == '__main__':
    main()




