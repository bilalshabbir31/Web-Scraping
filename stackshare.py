from bs4 import BeautifulSoup
import requests
import pandas as pd

response=requests.get("https://stackshare.io/feed")

webp=response.text


soup=BeautifulSoup(webp,"html.parser")

article=soup.find_all(name='a',class_='css-1wxqv74')


article_title=[score.getText().split()[0] for score in soup.find_all(name='a',class_='css-1wxqv74')]
article_get_votes_views=[score.getText().split()[0] for score in soup.find_all(name='span',class_='css-1j8ckqt')]


Extractvotes=[]

j=0
while j< len(article_get_votes_views):
    Extractvotes.append(article_get_votes_views[j])
    j=j+2


Extractviews=[]
q=1

while q< len(article_get_votes_views):
    Extractviews.append(article_get_votes_views[q])
    q=q+2


newarticleupview=[]
########## split votes
i=0
flag=False
for art in Extractviews:
    l=len(art)
    while i<l:
        if art[i]=='K':
            flag=True
            newarticleupview.append(float(art[:-1]))
        i=i+1
    i=0
    if flag==False:
        newarticleupview.append(float(art))
    else:
        flag=False


newview=[int(i) for i in newarticleupview]  #int views


newvotes=[int(i) for i in Extractvotes]  #int votes


d={'Title':article_title,'View':newview,'Votes':newvotes}

df=pd.DataFrame(data=d)

df.to_csv('Stack-Share.csv',index=False)

