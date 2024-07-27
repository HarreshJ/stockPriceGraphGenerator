import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import date

def askInput():
    tickerNames = []
    again = True
    asking = True
    while asking:
        ticker = input('Name (TICKER NAME): ')
        tickerNames.append(ticker)
        again = input('Add another? (Y/N): ').lower()
        if again != 'y':
            asking = False
    
    return tickerNames

def makeGraph(names):

    dataArray = []

    startDate = input('Enter the start date from which you would like to see the stock price (YYYY-MM-DD): ')

    plt.figure(figsize=(12, 6))

    for name in range(len(names)):
        data = yf.download(names[name], start=startDate, end=date.today())
        dataArray.append(data)
    
    for dataItem in dataArray:
        dataItem.index = pd.to_datetime(dataItem.index)

    index = 0

    for item in dataArray:
        plt.plot(item['Close'], label = names[index])
        index += 1

        

def showGraph():
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Prices')
    plt.legend()
    plt.grid(True)
    plt.show()


def run():

    print('Here are some common ticker names: AAPL (Apple), MSFT (Microsoft), AMZN (Amazon), NVDA (Nvidia), JPM (JP Morgan), MS (Morgan Stanley)')
        
    tickerNames = askInput()

    makeGraph(tickerNames)
    showGraph()

run()