from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

re=requests.get('https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv')

soup=BeautifulSoup(re.text,'html.parser')

title=soup.title.string

movies_content=soup.find_all('h3',attrs={'class':'lister-item-header'})

movies_name=[movies_content[i].a.string for i in range(len(movies_content))]


# print(movies_name)  #50 Movies Names

#############################################################
year_content=soup.find_all('span',attrs={'class':'lister-item-year text-muted unbold'})
release_years=[year_content[i].string for i in range(len(year_content))]
#print(release_years) #50 Release Years

############################################################

certificate=soup.find_all('span',attrs={'class':'certificate'})
# print(certificate[0].string)

movies_certificate=[certificate[i].string for i in range(len(certificate))]
i=42
while i<50:
    movies_certificate.append(None)
    i=i+1
# print(movies_certificate)    #50 certificate

############################################################

time=soup.find_all('span',attrs={'class':'runtime'})

runningtime=[time[i].string for i in range(len(time))]
#print(runningtime)            #50 runningtime

###########################################################

rating=soup.find_all('div',attrs={'class':'inline-block ratings-imdb-rating'})

movies_rating=[float(rating[i].strong.string) for i in range(len(rating))]
#print(movies_rating)          #50 movies rating

##########################################################

metascores=soup.find_all('div',attrs={'class':'inline-block ratings-metascore'})

movies_metascores=[int(metascores[i].span.string.strip()) for i in range(len(metascores))]
movies_metascores.insert(40,0)
#print(movies_metascores)       #50 metascores

##########################################################
votes=soup.find_all('span',attrs={'name':'nv'})

movies_votes=[int(votes[i].string.replace(',','')) for i in range(len(votes)) if (votes[i].string)[0]!='$']
#print(movies_votes)            #50 votes

#########################################################
gross=soup.find_all('p',attrs={'class':'sort-num_votes-visible'})


movies_gross=list()
for i in range(len(gross)):
    if len(gross[i].text.replace('\n','').split(' '))==2:
        string=gross[i].text.replace('\n','').split(' ')
        movies_gross.append(string[1][6:])
    else:
        movies_gross.append(None)

# print(movies_gross)             #50 Grosses

#########################################################
#                Creating-Dataset
########################################################

Dataset=pd.DataFrame(
    {
        'Name':movies_name,
        'Release_Year':release_years,
        'Certificate':movies_certificate,
        'Running_time':runningtime,
        'Rating':movies_rating,
        'MetaScores':movies_metascores,
        'Votes':movies_votes,
        'Gross':movies_gross
    }
)
# print(Dataset.head())

# Dataset.to_csv('IMDb-Top50.csv')

######################################################
#               Creating Databases
#####################################################

connection=sqlite3.connect('IMDb-Top50')
cursor=connection.cursor()

cursor.execute("Create table top50 (Name,Release_Year,Certificate,Running_time,Rating,MetaScores,Votes,Gross)")

for i in range(50):
    cursor.execute("insert into top50 values (?,?,?,?,?,?,?,?)",(movies_name[i],release_years[i],movies_certificate[i],runningtime[i],movies_rating[i],movies_metascores[i],movies_votes[i],movies_gross[i],))

cursor.execute("Select * from top50")
print(cursor.fetchall())
connection.commit()
connection.close()