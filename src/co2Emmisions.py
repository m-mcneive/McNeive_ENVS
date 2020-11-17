import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
This source had measurements of the carbon emissions of various countries. It also has measurements
of the continents as a whole. These are the measurements that I used because once visualized this will
be easier to read. The program below extracts just the values for the continents as a whole and plots
them on a line graph.

https://ourworldindata.org/co2-emissions
"""

#Reads the CSV
df = pd.read_csv('data/annual-co2-emissions-per-country (1).csv')
#Creates the list that will store the values to be used in the DataFrame
lst = []
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America']

#Iterates through all rows of the CSV
for row in df.iterrows():
    #Checks for rows involving continents as a whole
    if row[1][0] in continents:
        lst.append([row[1][0], row[1][2], row[1][3]])

data = pd.DataFrame(lst, columns = ['Continent', 'Year', 'Emissions'])
#Pivots the data to be better visualized
data = data.pivot(index='Year', columns='Continent', values='Emissions')
ax = data.plot(title = "CO2 emission by continent")
ax.set_ylabel("Billion tons of CO2")
plt.show()



