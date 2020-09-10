import requests
from bs4 import BeautifulSoup

fp = open("C:\\Users\\JK\\Documents\\Computer Network\\main_links.txt" , "r")

while fp:
    path="C:\\Users\\JK\\Documents\\Computer Network\\"
    url=''
    name=fp.readline().strip()
    if name=='':
        break
    path=path+name[30:-1]+'.htm'
    url=url+name
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'html.parser')
    ref=soup.find('div', { "class" : "site-content"})
    ref=ref.prettify("utf-8")
    with open(path , "wb") as file:
        file.write(ref)

