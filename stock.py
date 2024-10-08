# -*- coding: utf-8 -*-
"""Stock.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Rb32bd6W9aw19PDifDXHOtwrMaVIYUb
"""

import numpy as np #The Numpy numerical computing library
import pandas as pd #The Pandas data science library
import requests #The requests library for HTTP requests in Python
import math #The Python math module
from scipy import stats #The SciPy stats module

import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "TSLA", "META", "AMD", "CRM", "ASML"]
fields = ['ticker', 'Price', 'trailingPE', 'forwardPE', 'priceToBook', 'dividendYield', 'trailingEps',
          'forwardEps', 'marketCap', 'returnOnEquity', 'revenueGrowth', 'profitMargins', 'debtToEquity',
          'totalRevenue', 'netIncomeToCommon', '52weekhigh', '52weeklow', 'Open', 'Close', 'High', 'Low']

data = []

for ticker in tickers:
    info = yf.Ticker(ticker).info
    data.append([
        ticker,
        'N/A',
        info.get('trailingPE'),
        info.get('forwardPE'),
        info.get('priceToBook'),
        info.get('dividendYield'),
        info.get('trailingEps'),
        info.get('forwardEps'),
        info.get('marketCap'),
        info.get('returnOnEquity'),
        info.get('revenueGrowth'),
        info.get('profitMargins'),
        info.get('debtToEquity'),
        info.get('totalRevenue'),
        info.get('netIncomeToCommon'),
        info.get('fiftyTwoWeekHigh'),
        info.get('fiftyTwoWeekLow'),
        'N/A',
        'N/A',
        'N/A',
        'N/A'
    ])

all_data = pd.DataFrame(data, columns=fields)
all_data

import yfinance as yf
import pandas as pd

# Fields for the final DataFrame
hist_fields = ['ticker', 'Date', 'Volume', 'Price']

# Initialize the list to store data
dataf = []

# Iterate over each ticker
for ticker in tickers:
    # Get the historical data for the ticker
    hist = yf.Ticker(ticker).history(period='1y')

    # Iterate over DataFrame rows
    for index, row in hist.iterrows():
        data = {
            'ticker': ticker,
            'Date': index.strftime('%Y-%m-%d'),  # Format the date as needed
            'Volume': row['Volume'],
            'Price': 'N/A'
        }
        dataf.append([data[field] for field in hist_fields])

# Convert list to DataFrame
vol_price_df = pd.DataFrame(dataf, columns=hist_fields)

# Display the result
vol_price_df

data_price = yf.download(tickers,period='1y')['Adj Close']
for ticker in tickers:
    # Mask to filter rows for the current ticker
    mask = vol_price_df['ticker'] == ticker
    # Update the 'Price' column for rows corresponding to the current ticker
    vol_price_df.loc[mask, 'Price'] = vol_price_df.loc[mask, 'Date'].map(data_price[ticker])
vol_price_df

for ticker in tickers:
    # Fetch the historical data for the ticker (latest data)
    hist = yf.Ticker(ticker).history(period='1d')

    # Extract the Open, Close, High, Low values
    if not hist.empty:
        open_price = hist['Open'].values[0]
        close_price = hist['Close'].values[0]
        high_price = hist['High'].values[0]
        low_price = hist['Low'].values[0]

        # Update the corresponding row in all_data DataFrame
        all_data.loc[all_data['ticker'] == ticker, 'Open'] = open_price
        all_data.loc[all_data['ticker'] == ticker, 'Close'] = close_price
        all_data.loc[all_data['ticker'] == ticker, 'High'] = high_price
        all_data.loc[all_data['ticker'] == ticker, 'Low'] = low_price

# Print the updated DataFrame
all_data

pricer = []
l = ['Price']
for ticker in tickers:
  fp = yf.download(ticker,period='1d')['Adj Close']
  pricer.append(fp.iloc[0])
  all_data['Price'] = pd.DataFrame(pricer, columns=l)
# Print the updated DataFrame
all_data

