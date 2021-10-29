import requests
from bs4 import BeautifulSoup

res=requests.get('https://www.kaggle.com/datasets')

soup=BeautifulSoup(res.text,'html.parser')

print(soup)
#
# item=soup.select('.c16H9d')
# price=soup.select('.c3gUW0')
# # print(item)
