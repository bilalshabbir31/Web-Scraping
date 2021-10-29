import  pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint



res=requests.get('https://news.ycombinator.com/')


soup=BeautifulSoup(res.text,'html.parser')  # convert string to html

links=soup.select('.storylink')
subtext=soup.select(('.subtext'))

def sort_stories_by_votes(hnlist):
    return  sorted(hnlist,key=lambda k:k['votes'],reverse=True)


def create_custom_hn(links,subtext):
    hn=[]
    for idx,item in enumerate(links):
        title=item.getText()
        href=item.get('href',None)
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title':title,'link':href,'votes':points})
    return  sort_stories_by_votes(hn)


# pprint.pprint(create_custom_hn(links,subtext))


d=create_custom_hn(links,subtext)


title=[]
vote=[]


for i in d:
    title.append(i['title'])
    vote.append(i['votes'])


df=pd.DataFrame({'Title':title,'Votes':vote})
print(df)
df.to_csv('HackerNews.csv',index=False)


# d=[{'title':'bilal','age':25},{'title':'papa','age':55}]
#
# # print(d[0]['age'])
# # print(d['title'])
# age=[]
# title=[]
# j=0
# for i in d:
#     age.append(i['age'])
#     title.append(i['title'])
#
#
# df=pd.DataFrame({'Title':title,'Age':age})
# print(df)
#
# df.to_csv('db.csv',index=False)