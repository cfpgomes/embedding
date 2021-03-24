import yfinance as yf
import pandas as pd
import numpy as np
import json

N = 50

# The first N indexes in the wikipedia table are used as tickers.
# TODO: Change method of choosing stocks.
table = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
tickers = list(table[0]['Symbol'].sort_values())[:N]

convert_dot_to_dash_tickers = ['BF.B', 'BRK.B']

for i in range(len(tickers)):
    if tickers[i] in convert_dot_to_dash_tickers:
        tickers[i] = tickers[i].replace('.', '-')
        print(tickers[i])

print(str(N) + ' tickers used:')
print(tickers)

# The tickers' 1 year historical data is downloaded.
period = '1y'
interval = '1mo'
data = yf.download(tickers, period=period, interval=interval)['Adj Close']

# The data is then processed to drop NaN values, then to calculate percent
# change between months, and then to drop NaN values again.
data = data.dropna().pct_change().dropna()
print('Data:')
print(data)

# Mu is monthly expected return
mu = data.mean(0)
print('Mu:')
print(mu)

# Sigma is covariance between assets
sigma = data.cov(0)
print('Sigma:')
print(sigma)

# Export data to file
with open('data/outN{}.json'.format(N, B), 'w') as f:
    json.dump({
        'N': N,
        'tickers': tickers,
        'mu': mu.to_dict(),
        'sigma': sigma.to_dict(),
    }, fp=f, indent=4)
