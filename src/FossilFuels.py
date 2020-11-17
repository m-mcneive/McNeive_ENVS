import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

"""
https://datahub.io/core/co2-fossil-global
"""

df = pd.read_csv('data/FFSince1751.csv')

x = df.Year
y = df.GasFuel

stats = linregress(x, y)
#print(stats)

m = stats.slope
b = stats.intercept


ax = df.plot(x = 'Year', title = "Fossil Fuel use globally")
ax.set_ylabel("Million metric tons of C")
plt.show()

