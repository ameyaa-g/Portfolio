
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         AMEYA GOPINATH
# Section:      M02
# Assignment:   11 LAB
# Date:         11/23/23
#

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from datetime import datetime
import pandas as pd
from dateutil import relativedelta

with open('WeatherDataCLL.csv', 'r') as my_file:
    lines = my_file.readlines()

newlist = []
for a in lines:
    noNew = a.replace('\n', '')
    newlist.append(noNew)


data = []
for i in range(len(newlist)):
    a = newlist[i].split(',')
    data.append(a)


x = []
mph = []
y2 = []
prec = []
hum = []
month = []
avg = []
mina = []

matrix = np.array(data)
start = datetime.strptime(matrix[1][0], '%m/%d/%Y')

for i in range(len(matrix)):
    if i > 1:
        currdate = datetime.strptime(matrix[i][0], '%m/%d/%Y')
        delta = currdate - start
        x.append(delta.days)
        r = relativedelta.relativedelta(currdate, start)
        mon = r.months + (12 * r.years)
        month.append(mon)
        if matrix[i][1] == '':
            y2.append(0)
        else:
            y2.append(float(matrix[i][1]))
        if matrix[i][2] == '':
            prec.append(0)
        else:
            prec.append(float(matrix[i][2]))
        if matrix[i][3] == '':
            hum.append(0)
        else:
            hum.append(float(matrix[i][3]))
        if matrix[i][4] == '':
            avg.append(0)
        else:
            avg.append(float(matrix[i][4]))
        if matrix[i][5] == '':
            mph.append(0)
        else:
            mph.append(int(matrix[i][5]))
        if matrix[i][6] == '':
            mina.append(0)
        else:
            mina.append(int(matrix[i][6]))
# first line graph
fig, ax1 = plt.subplots()
ax1.plot(x, mph, color = 'red')
ax2 = ax1.twinx()
ax2.plot(x, y2, color = 'blue')
ax1.title.set_text('Maximum Temperature and Average Wind Speed')
ax2.set_ylabel('Average Wind Speed, mph')
ax1.set_ylabel('Maximum Temperature, F')
ax1.set_xlabel('Date')


# histogram
fig1, histo = plt.subplots(1)

start, end = histo.get_xlim()
histo.xaxis.set_ticks(np.arange(0, 25, 2.5))
histo.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
histo.hist(y2, bins = 30, edgecolor='black', linewidth=1.2, facecolor = 'green')
histo.title.set_text('Histogram of Average Wind Speed')
histo.set_xlabel('Average Wind Speed, mph')
histo.set_ylabel('Number of days')


# dot plot

fig2, scat = plt.subplots()
scat.set_xlim(left=30, right=100)
scat.xaxis.set_ticks(np.arange(30, 100, 10))
scat.scatter(hum, prec, color='black')
scat.title.set_text('Precipitation Vs. Average Relative Humidity')
scat.set_xlabel('Average Relative Humidity (%)')
scat.set_ylabel('Precipitation (in)')

# bar graph

# find highes high and lowest low of each mont
maxloc = []
minloc = []
dy = []
dx = []

fig3, barg = plt.subplots()
barg.bar(month, height=avg)
for i in range(len(month)//30 - 1):
    if i != 0:
        dy = dy + mph[(i*30):((i+1)*30)]
        dx = dx + mina[:((i + 1) * 30)]
    else:
        dy = dy + mph[:((i + 1) * 30)]
        dx = dx + mina[:((i + 1) * 30)]
    maxloc.append(max(dy))
    minloc.append(min(dx))


month = list(set(month))
high, = barg.plot(month, maxloc, color = 'red')
low, = barg.plot(month, minloc, color = 'blue')
barg.title.set_text('Temperature By Month')
barg.set_ylabel('Average Temperature, F')
barg.set_xlabel('Month')
high.set_label('High Temp')
low.set_label('Low Temp')
barg.legend(loc = 'upper right')

plt.show()



