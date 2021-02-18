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

response = get('http://licznikapostazji.pl')
soup = BeautifulSoup(response.content, "html.parser")


print(soup.get_text('\n'))
