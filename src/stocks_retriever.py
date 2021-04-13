import yfinance as yf
import pandas as pd
import numpy as np
import json
from datetime import datetime

N = 8

# The first N indexes in the wikipedia table are used as tickers.
# TODO: Change method of choosing stocks.
table = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

table = table[0]
print(table[lambda x: x['GICS Sector'] == 'Communication Services'])

tickers = None

dataset_type = 'strongly_correlated'

banned_tickers = ['FOXA', 'FB']

if dataset_type == 'alphabetical':
    tickers = list(table['Symbol'].sort_values())[:N]
elif dataset_type == 'diversified':
    sectors = list(np.unique(table['GICS Sector']))
    taboo_subsectors = []
    tickers = []
    while len(tickers) < N:
        for sector in sectors:
            for index, row in table[lambda x: x['GICS Sector'] == sector].iterrows():
                if (row['Symbol'] not in tickers) and (row['GICS Sub-Industry'] not in taboo_subsectors) and (row['Symbol'] not in banned_tickers):
                    tickers.append(row['Symbol'])
                    taboo_subsectors.append(row['GICS Sub-Industry'])
                    break
            if len(tickers) == N:
                break
elif dataset_type == 'strongly_correlated':
    sectors = list(np.unique(table['GICS Sector']))
    tickers = []
    while len(tickers) < N:
        for sector in sectors:
            for index, row in table[lambda x: x['GICS Sector'] == sector].iterrows():
                if (row['Symbol'] not in tickers) and (row['Symbol'] not in banned_tickers):
                    tickers.append(row['Symbol'])
                    if len(tickers) == N:
                        break
            if len(tickers) == N:
                break
print(tickers)
convert_dot_to_dash_tickers = ['BF.B', 'BRK.B']

for i in range(len(tickers)):
    if tickers[i] in convert_dot_to_dash_tickers:
        tickers[i] = tickers[i].replace('.', '-')
        print(tickers[i])

print(str(N) + ' tickers used:')
print(tickers)

# The tickers' 1 year historical data is downloaded.
period = '1mo'
interval = '1d'
data = yf.download(tickers, period=period, interval=interval)['Adj Close']
print('Data:')
print(data)

print('debug:')
for t in tickers:
    print(data[t])

# The data is then processed to drop NaN values, then to calculate percent
# change between months, and then to drop NaN values again.
data = data.dropna().pct_change().dropna()
print('Data processed:')
print(data)

print('Tickers:')
print(list(data.columns))

# Mu is monthly expected return
mu = data.mean(0)
print('Mu:')
print(mu)

# Sigma is covariance between assets
sigma = data.cov(0)
print('Sigma:')
print(sigma)


# Get timestamp
date_obj = datetime.now()
date = 'Y{:04}M{:02}D{:02}h{:02}m{:02}s{:02}'.format(
    date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second)

# Export data to file
with open(f'data/out_{dataset_type}_N{N}_p{period}_i{interval}.json', 'w') as f:
    json.dump({
        'N': N,
        'period': period,
        'interval': interval,
        'tickers': list(data.columns),
        'date': date,
        'mu': mu.to_dict(),
        'sigma': sigma.to_dict(),
    }, fp=f, indent=4)
