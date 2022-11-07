from bs4 import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("https://guides.hsl.virginia.edu")
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(links)
