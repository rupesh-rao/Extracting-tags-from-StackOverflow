from urllib.request import urlopen
from bs4 import BeautifulSoup

filename = 'stackoverflow_tags.csv'
f = open(filename,'w')

headers = "Tags\n"
f.write(headers)

page_start = 1
page_end = 1538
for i in range(page_start,page_end + 1):
    url = "https://stackoverflow.com/tags?page="+str(i)+"&tab=popular"
    furl = urlopen(url)
    html = furl.read()
    furl.close()

    soup = BeautifulSoup(html,'html.parser')

    containers =  soup.findAll('div',{'class':'grid-layout--cell tag-cell'})

    for container in containers:
        tag = container.a.text
        
        f.write (tag +"\n")
    
