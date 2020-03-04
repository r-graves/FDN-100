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

def get_site(soup,tag):
    tag_back = []
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'site':
                    x3 = x2.string.strip()
                    tag_back.append(x3)
    return tag_back

def get_variety(soup,tag):
    tag_back = []
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'variety':
                    x3 = x2.string.strip()
                    tag_back.append(x3)
    return tag_back

def get_y1(soup,tag):
    tag_back = []
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'Y1':
                    x3 = x2.string.strip()
                    tag_back.append(x3)
    return tag_back

def get_y2(soup,tag):
    tag_back = []
    for x in soup.find_all('div'):
        if x.get('id') == 'barley-data':
            x1 = x
            for x2 in x1.find_all('div'):
                if x2.get('id') == 'Y2':
                    x3 = x2.string.strip()
                    tag_back.append(x3)
    return tag_back


#create an output file




#main funciton controls everything
def write_out():
    url = get_url()
    tags_in = tag_ui()
    # use requests to get the url
    response = requests.get(url)
    # get the content from the response
    content = response.content
    #variable dictionary
    var_dict = get_var(BeautifulSoup(content, 'lxml'),tags_in)
    #site dictionary
    sites_dict = get_sites(BeautifulSoup(content, 'lxml'),tags_in)
    #data dictionary
    site_list = get_site(BeautifulSoup(content, 'lxml'), tags_in)
    variety_list = get_variety(BeautifulSoup(content, 'lxml'), tags_in)
    y1_list = get_y1(BeautifulSoup(content, 'lxml'), tags_in)
    y2_list = get_y2(BeautifulSoup(content, 'lxml'), tags_in)
    x = 0
    fout = open('hw7_out.txt', 'w')
    while x < len(y1_list):
        site_in = sites_dict.get(site_list[x])
        variety_in = var_dict.get(variety_list[x])
        out_line = str(site_in+','+variety_in +','+y1_list[x]+','+y2_list[x]+'\n')
        fout.write(out_line)
        x = x + 1
    fout.close()


#below runs the program
if __name__ == '__main__':
    write_out()




