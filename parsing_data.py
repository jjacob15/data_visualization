import csv
import  matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_07-2018_simple.csv"
highs=[]
lows=[]
dates=[]
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        highs.append(int(row[5]))
        lows.append(int(row[6]))
        dates.append(datetime.strptime(row[2],'%Y-%m-%d'))

fig,ax = plt.subplots()
ax.plot(dates,highs,c="red",alpha=0.5)
ax.plot(dates,lows,c="blue",alpha=0.5)

fig.autofmt_xdate()
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()