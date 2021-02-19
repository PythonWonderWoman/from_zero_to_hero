#!/usr/bin/env Python3

"""

exercise 3

how to start?
        - go to http://licznikapostazji.pl/ page and try to retrieve
        base of users mentioned on the page
        - see page in view source mode to see if you can see list of users in html component
        - you will need 'get' module from 'reqests'
        - now we need to convert www url to html
        - use bs4 from BeautifulSoup module
        - and parse url
        
"""
from requests import get
from bs4 import BeautifulSoup

# database will be extracted from html request
response = get('http://licznikapostazji.pl')

# parse html content
soup = BeautifulSoup(response.content, "html.parser")

# extract only <h3> tags and remove unnecessary html content
tags = BeautifulSoup.findAll(soup, 'h3')

for line in tags:
    # tags to separatate lines, replace . and spaces and prepare data for csv file
    output = line.text.strip().replace('. ',',').replace(", ",",").replace(".,",",")
    # print only lines starting with integer 
    if output.startswith('1') or output.startswith('2') or output.startswith('3') or output.startswith('4') or output.startswith('5') \
       or output.startswith('6') or output.startswith('7') or output.startswith('8') or output.startswith('9') or output.startswith('0') == True:
        print(output, end='\n')

    
