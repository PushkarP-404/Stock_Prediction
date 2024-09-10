import datetime as dt
import pandas as pd

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


end = dt.datetime.now()
start = end - dt.timedelta(days=365)
start, end

#StockList = ['HDFCBANK','ICICIBANK']
#Stocks = [i + '.NS' for i in StockList]


data = pdr.DataReader("HDFCBANK.NS")
data.to_csv("HDFC_data.csv")

#df = pdr.get_data_yahoo(Stocks, start, end)
#print(df.head())
