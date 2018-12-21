from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/tutorial/')
bs = BeautifulSoup(html.read(), 'html.parser')
subdomainlist = bs.findAll('div', {'class': 'subtopic-name darker regular weight-700 pointer'} ,text = True)
with open('subdomain_basics.txt', 'w') as f:
    for item in subdomainlist:
        f.write("%s\n" % item.get_text())
