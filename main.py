import requests
import bs4
res=requests.get('https://www.flipkart.com/')

soup=bs4.BeautifulSoup(res.text,'lxml')

hi=soup.select('title')

print(hi[0].getText())


hi.split('')