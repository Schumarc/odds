from urllib import request 
import time
import re

page_content=[]
url_requested = request.urlopen("https://www.tipico.de/de/online-sportwetten/fussball/deutschland/bundesliga/g42301/")
if(url_requested.code == 200):
    html_content = str(url_requested.read())
    file = open('test.txt','w') 
    file.write(html_content)