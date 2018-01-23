import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import csv

#Split the dataset into arrays for date, price and active users
with open('data.csv', 'r') as n:
    reader = csv.reader(n)
    header = next(reader)
    dates = []
    bitcoin_price = []
    active_users = []
    for row in reader:
    	active_users.append(int(row[0]))
    	bitcoin_price.append(float(row[1]))
    	dates.append(mdates.date2num(dt.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')))

#Active Users Axis
fig, ax1 = plt.subplots()
ax1.set_xlabel('Time (GMT+1): 22-01-2018 / 23-01-2018')
ax1.set_ylabel('Active Users on r/bitcoin', color='b')
ax1.tick_params('y', colors='b')
ax1.xaxis.set_major_locator(mdates.HourLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax1.plot(dates,active_users, 'b-')

#Bitcoin Price Axis
ax2 = ax1.twinx()
ax2.set_ylabel('Bitcoin Price (USD)', color='g')
ax2.tick_params('y', colors='g')
ax2.plot(dates,bitcoin_price,'g-')

#Plot configuration

plt.gcf().autofmt_xdate()
plt.title('Bitcoin Price in USD and r/bitcoin Active Users over the same period of time (by u/legendary_miner)\n ',fontsize=12)
fig.suptitle('RedditMarketCap\n ', fontsize=20)

plt.show()