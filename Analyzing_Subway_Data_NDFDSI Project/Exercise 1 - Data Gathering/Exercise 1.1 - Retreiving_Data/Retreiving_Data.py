## NOTE ------>  IF YOU HAVE NOT READ THE 'README.TXT' FILE , KINDLY GO BACK AND READ IT. IT WILL BE HELPFUL ##

'''
Exercise 1.1        RETRIEVING DATA FROM URL

Problem Statement :

Let's do it!! Now it's your turn to gather data. Please write bellow a Python code to access the link http://web.mta.info/developers/turnstile.html and download all files from June 2017. The file must be named turnstile_100617.txt, where 10/06/17 is the file's date.

Please see below a few commands that might help you:

Use the urllib library to open and redeem a webpage. Use the command below, where url is the webpage path to the following file:

u = urllib.urlopen(url)
html = u.read()
Use the BeautifulSoup library to search for the link to the file you want to donwload in the page. Use the command below to create your soup object and search for all 'a' tags in the document:

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all('a')
A tip to only download the files from June is to check data in the name of the file. For instance, to donwload the 17/06/2017 file, please see if the link ends with "turnstile_170610.txt". If you forget to do this, you will download all files from that page. In order to do this, you can use the following command:

if '1706' in link.get('href'):
Our final tip is to use the command bellow to download the txt file:

urllib.urlretrieve(link_do_arquivo, filename)
Please remember - you first have to load all packages and functions that will be used in your analysys.

'''




# Solution :

import urllib
import urllib.request
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
u = urllib.request.urlopen(url)
html = u.read()
soup = BeautifulSoup(html,'html.parser')
links = soup.find_all('a')
for i in links:
        ref = i.get('href')     													# Point 1
        if ref is not None and "1706" in ref:  
             filename = "turnstile_" + ref[-6:-4]+ref[-8:-6]+ref[-10:-8]+".txt"     # Point 2
             url_to_fetch = "http://web.mta.info/developers/"+ ref    				# Point 3
             urllib.request.urlretrieve(url_to_fetch,filename)




'''
KEY POINTS

1. 	i.get('href) fetches the href part of <a> tag..something like  /data/nyct/turnstile/turnstile_170824.txt
2. 	Changing the end part of the filename from yy/mm/dd to dd/mm/yy .    string[-x:-y] slices the string from end. end character has index -1 . End result will be
	something like 		eg. turnstile_170824.txt to turnstile_240817.txt
3. 	This gives the complete url ..from where the file is to be downloaded
'''