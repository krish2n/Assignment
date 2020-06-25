# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:18:59 2020

@author: HP
"""


from yahoofinancials import YahooFinancials
import datetime as dt
import pandas as pd

all_tickers=["MSFT","IRCTC.NS","TCS.NS"]
start_date=(dt.datetime.today()-dt.timedelta(60)).strftime('%Y-%m-%d')
end_date=(dt.datetime.today()-dt.timedelta(1)).strftime('%Y-%m-%d')
cl_price=pd.DataFrame()

ticker="IRCTC.NS"
for ticker in all_tickers:
    yahoo_financial=YahooFinancials(ticker)
    data=yahoo_financial.get_historical_price_data(start_date, end_date, "daily")
    ohlv=data[ticker]["prices"]
    temp=pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
    temp.set_index("formatted_date",inplace=True)
    temp.dropna(inplace=True)
    cl_price[ticker]=temp["adjclose"]
    
