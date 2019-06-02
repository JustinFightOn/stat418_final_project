# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:54:28 2019

@author: Cyndi
"""


import requests
import json
import pandas as pd
import urllib.parse
import numpy as np
from pmdarima.arima import auto_arima

with open('scripts/api_key.txt', 'r') as f:
    api_key = f.read()
main_url = 'https://www.alphavantage.co/query?'

date_index = ['2019-05-31', '2019-06-03', '2019-06-04', '2019-06-05', '2019-06-06', '2019-06-07', 
         '2019-06-10', '2019-06-11', '2019-06-12', '2019-06-13', '2019-06-14',
         '2019-06-17', '2019-06-18', '2019-06-19', '2019-06-20', '2019-06-21',
         '2019-06-24', '2019-06-25', '2019-06-26', '2019-06-27', '2019-06-28',
         '2019-07-01', '2019-06-02', '2019-07-03', '2019-07-05']

def get_stock_data_in_json(stock):
    url = main_url + urllib.parse.urlencode({'function': 'TIME_SERIES_DAILY', 'symbol': stock, 'apikey': api_key})
    response = requests.get(url)
    if response.status_code != 200:
        print('Invalid input, please try again.')
        return {}
    return json.loads(response.content)

def convert_json_to_dataframe(json_data):
    df = pd.DataFrame(json_data['Time Series (Daily)']).T
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.apply(pd.to_numeric)
    df.sort_index(inplace=True)
    return df

def predict(stock, n=7):

    json_data = get_stock_data_in_json(stock)
    df = convert_json_to_dataframe(json_data)
    header = json_data['Meta Data']
    
    high = df.iloc[:,1]
        
    model = auto_arima(high, trace=True, error_action='ignore', suppress_warnings=True)
    model.fit(high)
    
    pred = model.predict(n_periods=n)
    pred = np.round(pred, 2)
    
    prev = dict(high[-n:])
    furture_dates = [i for i in date_index if i > header['3. Last Refreshed']]
    forecast = dict(zip(furture_dates[:n], pred))
    
    result = {'Stock': header['2. Symbol'], 'Last Refreshed': header['3. Last Refreshed'],
              'Previous Stock Price': prev, 'Forecasted Stock Price': forecast}
    return result