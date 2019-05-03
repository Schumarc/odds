from urllib import request 
import time

url_requested = request.urlopen("https://www.tipico.de/de/online-sportwetten/fussball/deutschland/bundesliga/g42301/")
if(url_requested.code == 200):
    html_content = str(url_requested.read())
    print(html_content)
    time.sleep(100)