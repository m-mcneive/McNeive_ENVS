import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
    This file tracks temperature changes from 1880 to 2016.

    https://datahub.io/core/global-temp#readme
"""

df = pd.read_csv('data/globalTempPerMonth.csv')

"""
The data will be split into the 2 groups that recorded it.

GCAG = Climate at a Glance
GISTEMP = GISS Surface Temperature
"""

GCAG = pd.DataFrame(columns=['Date', 'Mean'])
GISTEMP = pd.DataFrame(columns=['Date', 'Mean'])

#Iterates through full dataframe, splitting it into 2 parts
for row in df.iterrows():
    dictionary = {'Date': row[1][1][:4], 'Mean': row[1][2]}
    #print(row[1][1][:4])
    if row[1][0] == "GCAG":
        GCAG = GCAG.append(dictionary, ignore_index=True)
    else:
        GISTEMP = GISTEMP.append(dictionary, ignore_index=True)

#Reverses DataFrame, the CSV has most recent data first, reverse improves visualization
GCAG = GCAG.reindex(index=GCAG.index[::-1])
GISTEMP = GISTEMP.reindex(index=GISTEMP.index[::-1])

x = GCAG.Date
y = GCAG.Mean 

a = GISTEMP.Date 
b = GISTEMP.Mean 


GCAG.plot(x = 'Date', title = 'GCGA')
GISTEMP.plot(x = 'Date', color = 'red', title = 'GISTEMP')
plt.show()

