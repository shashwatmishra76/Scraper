from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.hackerearth.com/practice/algorithms/searching/linear-search/tutorial/')
bs = BeautifulSoup(html.read(), 'html.parser')
subdomainlist = bs.findAll('div', {'class': 'subtopic-name darker regular weight-700 pointer'} ,text = True)
with open('subdomain_algo.txt', 'w') as f:
    for item in subdomainlist:
        f.write("%s\n" % item.get_text())
