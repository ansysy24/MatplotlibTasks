from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('ages.csv')
ages = data['Age']
bins = range(0, 110)
plt.hist(ages, bins=bins, edgecolor='black', log=True)
plt.show()
