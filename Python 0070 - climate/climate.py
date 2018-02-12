import matplotlib.pyplot as plt
from datetime import date
import csv
import json
    
with open('GlobalTemperatures.csv') as csvfile:
    data = list(csv.DictReader(csvfile))[160:]
    
    dates = [date(*[int(n) for n in row['dt'].split('-')])  for row in data]
    temps = [round(float(row['LandAverageTemperature']), 2) for row in data]

axes = plt.gca()
axes.set_ylim([9, 14])
plt.bar(dates[::60], temps[::60], width=1200)
plt.title('Average Land Temperatures')
plt.xlabel('Date')
plt.ylabel('Average Temp (C)')

plt.xticks()
plt.show()
