import requests as req
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

html = req.get("https://www.worldometers.info/coronavirus")
html.content
html_parsed = BeautifulSoup(html.content)
table = html_parsed.find('table', attrs={'id': 'main_table_countries_today'})
rows = table.find_all("tr")
rows[0].text.strip()
rows[9].text.strip().split("\n")
data = []
for x in rows:
    data.append(x.text.strip().split("\n")[1:5]) #primeiras nove colunes
df = pd.DataFrame(data)
print(df.head())
df = pd.DataFrame(data[9:], columns=data[0])
print(df.head())
df.to_csv('covid19.csv')
df_plot = df[['Country,Other', 'TotalCases']]

df_plot = df_plot[:10]
df_plot.head()
df_plot['TotalCases'] = df_plot['TotalCases'].apply(lambda x: x.replace(',','')).astype(int)
df_plot.head()
df_plot.plot(kind ='bar', x='Country,Other', y='TotalCases')
print(df_plot.head())
