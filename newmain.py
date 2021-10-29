from bs4 import BeautifulSoup
import requests
import pandas as pd

reponse=requests.get("https://news.ycombinator.com/")

webp=reponse.text


soup=BeautifulSoup(webp,"html.parser")



article=soup.find_all(name='a',class_="storylink")

article_texts=[]
article_links=[]
article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]


j=0
for arts in article:
    if j < len(article_upvotes):
        texts=arts.getText()
        article_texts.append(texts)
        links=arts.get("href")
        article_links.append(links)
        j=j+1





# max_votes=max(article_upvotes)    geting largest votes
# print(article_upvotes.index(max_votes))



d={'Title':article_texts,'Upvotes':article_upvotes}

Data=pd.DataFrame(data=d)
print(Data)
Data.to_csv("HackerNew-Data.csv",index=False)


# RS=(int(article_upvotes[0].split()[0]))
#
# print(RS)
# print(type(RS))