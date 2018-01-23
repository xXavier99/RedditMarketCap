import requests
import json
import csv
import datetime
import time
from tabulate import tabulate

def get_active_users(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers={"User-Agent": "r/bitcoin active user count related to bitcoin price"})
    if not resp.ok:
        
        return -1
    content = resp.json()
    return content["data"]["accounts_active"]

def getBitcoinPrice():

    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/bitcoin"

    
    request = requests.get(tickerURL)
    data = request.json()

    ticker = data[0]['symbol']
    price = data[0]['price_usd']
    return price

def writeData():
	file = open("data.csv","a", newline='')
	active_users = get_active_users('bitcoin')
	bitcoin_price = getBitcoinPrice()
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	write_file = csv.writer(file)
	write_file.writerow([active_users,bitcoin_price,now])
	print (tabulate([['Active Users r/bitcoin', 'BTC Price in USD', 'Date'],[active_users,bitcoin_price,now]], headers="firstrow"))
	
while True:
	writeData()
	time.sleep(300)