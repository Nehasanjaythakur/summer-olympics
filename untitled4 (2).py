# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l3IMKb73ikIDspyEtD8kqCCkkdFa-A_Y
"""



"""1. In how many cities Summer Olympics is held so far?"""

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

df['City'].unique()

"""2. Which sport is having most number of medals so far? (Top 5)"""

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Medal in df['Sport'].unique():
  data.append([Medal , len(df[df['Sport'] == Medal])])

data = pd.DataFrame(data, columns = ['Sport','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Sport', y = 'freq', kind = 'bar')



"""3.Which sport is having most number of Gold Medals so far? (Top 5)"""

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Medal in df['Medal'].unique():
  data.append([Medal , len(df[df['Medal'] == Medal])])

data = pd.DataFrame(data, columns = ['Medal','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Medal', y = 'freq', kind = 'bar')

"""4. Which player has won most number of medals? (Top 5)"""

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Medal in df['Gender'].unique():
  data.append([Medal , len(df[df['Gender'] == Medal])])

data = pd.DataFrame(data, columns = ['Medal','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Medal', y = 'freq', kind = 'bar')

5. Which player has won most number Gold Medals of medals? (Top 5)

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Medal in df['Athlete'].unique():
  data.append([Medal , len(df[df['Athlete'] == Medal])])

data = pd.DataFrame(data, columns = ['Athlete','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Athlete', y = 'freq', kind = 'line')



"""6. In which year India won first Gold Medal in Summer Olympics?"""

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Medal in df['Year'].unique():
  data.append([Medal , len(df[df['Year'] == Medal])])

data

7. Which event is most popular in terms on number of players? (Top 5)

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Athlete in df['Event'].unique():
  data.append([Athlete , len(df[df['Event'] == Athlete])])

data = pd.DataFrame(data, columns = ['Event','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Event', y = 'freq', kind = 'line')

8. Which sport is having most female Gold Medalists? (Top 5)

import pandas as pd

df = pd.read_csv ("5_6190749518103839648.csv")

df

data = []
for Event in df['Gender'].unique():
  data.append([Event , len(df[df['Gender'] == Event])])

data = pd.DataFrame(data, columns = ['Gender','freq'])
data = data.sort_values(by = 'freq', ascending = False).head()

data.plot(x = 'Gender', y = 'freq', kind = 'bar')

