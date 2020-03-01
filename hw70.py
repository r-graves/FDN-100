"""Going for the Immer HTML to CSV goal, since I was just working with CSV's on HW 8"""
"""from the index file I will create a dictionary
based on tag, read from the dictoonary, and write the output
to a csv file"""
import requests
from bs4 import BeautifulSoup
import csv

#get the website coming in
def get_url():
    url = "https://raw.githubusercontent.com/denisemauldin/immer/master/index.html"
 #  url = input("Please specify a URL: ")
    return(url)
#get the tags coming in
def tag_ui():
    #tags_in = input("Please specify what tag you are looking for: ")
    tags_in = 'div'
    return(tags_in)

#get_tags does the heavy lifting, using soup to drill down to the tag we are looking for
def get_sites(soup,tag):
    tag_back = {}
    #get the sites
    for x in soup.find_all('div'):
            if x.get('id') == 'site-legend':
                x1 = x
                for x2 in x1.find_all('div'):
                    if x2.get('id') == 'site':
                        tag_out = x2.string.strip()
                        tag_list = tag_out.split(' = ')
                        tag_back.update({tag_list[0]:tag_list[1]})
    return tag_back
def get_var(soup,tag):
    tag_back = {}
    #get the varities
    for x in soup.find_all('div'):
            if x.get('id') == 'variety-legend':
                x1 = x
                for x2 in x1.find_all('div'):
                    if x2.get('id') == 'variety':
                       x3 = x2.string.strip()
                       x4 = x3.split(' = ')
                       tag_back.update({x4[0]: x4[1]})
    return tag_back

def get_data(soup,tag):
    tag_back = {}
    d1 = {}
    d2 = {}
    variety = []
    site = []
    y1 = []
    y2 = []
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'site':
                    x3 = x2.string.strip()
                    site.append(x3)
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'variety':
                    x3 = x2.string.strip()
                    variety.append(x3)

    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'Y1':
                    x3 = x2.string.strip()
                    y1.append(x3)

    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'Y2':
                    x3 = x2.string.strip()
                    y2.append(x3)

    x = 0
    while x < len(site):
        v1 = y1[x]
        v2 = y2[x]
        d1.update({v1:v2})
        s = site[x]
        v = variety[x]
        d2.update({s:v})
        x = x + 1
    tag_back = {**d2, **d1}
    return tag_back


#create an output file
def write_out(tag_back):
    with open('hw70.txt', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in tag_back.items():
            writer.writerow([key, value])

#main funciton controls everything
def main():
    url = get_url()
    tags_in = tag_ui()
    # use requests to get the url
    response = requests.get(url)
    # get the content from the response
    content = response.content
    #variable dictionary
    var_dict = get_var(BeautifulSoup(content, 'lxml'),tags_in)
    #site dictionary
    site_dict = get_sites(BeautifulSoup(content, 'lxml'),tags_in)
    #data dictionary
    data_dict = get_data(BeautifulSoup(content, 'lxml'), tags_in)
    dict3 = {**site_dict, **var_dict}
    dict4 = {**dict3, **data_dict}
    write_out(dict4)






#below runs the program
if __name__ == '__main__':
    main()




