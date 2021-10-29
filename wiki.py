from bs4 import BeautifulSoup
import requests
import pandas as pd

re = requests.get('https://en.wikipedia.org/wiki/World_population')

soup = BeautifulSoup(re.text, "html.parser")

top = soup.select_one('tbody')

atag = top.find_all(name='a')
#
# print(atag[3].get('title'))
###############################################################
# Country
###############################################################
country = []
country.append(atag[2].get('title'))
i = 0
for a in atag:

    if a.get('title') is not None and i % 2 != 0 and i != 3:
        country.append(a.get('title'))
    i = i + 1

table = top.find_all(name='tr')

###############################################################
# Ranks
###############################################################


getranks = [t.text.split()[0] for t in table]

# print(f'getranks: {getranks}')      #14 index in list
rankslicing = getranks[2:12]
# print(f'ranks Slicing: {rankslicing}')


j = 0
ranks = []
while j < len(rankslicing):
    ranks.append(int(rankslicing[j]))
    j = j + 1

print(f'Countries: {country}')
print(f'ranks: {ranks}')

###############################################################
                # 2020 Population
###############################################################

Twenty2020 = [t.text.split()[2] for t in table]

Twenty2020=Twenty2020[2:14]

result=filter(lambda x:x!='States',Twenty2020)
Twenty2020=None
Twenty2020=list(result)
print(f'Twenty2020: {Twenty2020}')
###############################################################
                # 2015 Population
###############################################################
Twenty2015=[t.text.split()[3] for t in table]
Twenty2015=Twenty2015[2:13]
print(f'Twenty2015: {Twenty2015}')

###############################################################
                # 2030 Population
###############################################################

Twenty2030=[t.text.split()[4] for t in table]
Twenty2030=Twenty2015[2:13]
print(f'Twenty2030: {Twenty2030}')

###############################################################
                # Converting to CSV file
###############################################################



print(len(Twenty2020))
print(len(Twenty2015))
Twenty2030.append('0')
Twenty2030.append('0')
print(len(Twenty2030))
print(len(country))
ranks.append('0')
print(len(ranks))

d={'Countries':country,'Ranks':ranks,'Twenty2015':Twenty2015,'Twenty2020':Twenty2020,'Twenty2030':Twenty2030}

df=pd.DataFrame(data=d)

df.to_csv('World-population.csv',index=False)