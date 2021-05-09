import yfinance as yf
import pandas as pd
import numpy as np
import json
from datetime import datetime

for N in [8, 16, 32]:
    for dataset_type in ['diversified', 'correlated']:

        # The first N indexes in the wikipedia table are used as tickers.
        # TODO: Change method of choosing stocks.
        table = pd.read_html(
            'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

        table = table[0]
        #print(table[lambda x: x['GICS Sector'] == 'Communication Services'])

        tickers = None

        banned_tickers = ['FOXA', 'FB']
        convert_dot_to_dash_tickers = ['BF.B', 'BRK.B']

        if dataset_type == 'alphabetical':
            tickers = list(table['Symbol'].sort_values())[:N]
        elif dataset_type == 'industry_diversified':
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
        elif dataset_type == 'industry_correlated':
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
        elif dataset_type == 'correlated':
            # Get all tickers
            all_tickers = list(table['Symbol'])

            # Remove banned tickers
            for t in banned_tickers:
                all_tickers.remove(t)

            # Convert dots to dashes in certain tickers
            for i in range(len(all_tickers)):
                if all_tickers[i] in convert_dot_to_dash_tickers:
                    all_tickers[i] = all_tickers[i].replace('.', '-')
                    # print(all_tickers[i])

            # The tickers' 1 year historical data is downloaded.
            period = '1mo'
            interval = '1d'
            data = yf.download(all_tickers, period=period,
                               interval=interval)['Adj Close']
            data = data.dropna()
            print('debug1:')
            null_tickers = []
            for t in all_tickers:
                if data[t].isnull().values.any():
                    print(data.pop(t))
                    null_tickers.append(t)
                elif data[t].empty:
                    print(data.pop(t))
                    null_tickers.append(t)

            # Remove banned tickers
            for t in null_tickers:
                all_tickers.remove(t)

            # The data is then processed to drop NaN values, then to calculate percent
            # change between months, and then to drop NaN values again.
            data = data.pct_change().dropna()

            # Mu is monthly expected return
            mu = data.mean(0)

            # Sigma is covariance between assets
            sigma = data.cov(0)

            # corr_matrix is correlation between assets
            corr_matrix = data.corr()

            highest = all_tickers[:N]
            highest_score = float('-inf')

            debugvar = 0
            for starting_ticker in all_tickers:
                debugvar += 1
                print('TRY ' + str(debugvar))
                remaining_tickers = list(all_tickers)
                tickers = set()
                tickers.add(starting_ticker)
                remaining_tickers.remove(starting_ticker)

                while(len(tickers) != N):
                    ticker_to_add = None
                    ticker_to_add_score = float('-inf')
                    
                    for r in remaining_tickers:
                        r_score = 0
                        for t in tickers:
                            r_score += corr_matrix[r][t]
                        if r_score > ticker_to_add_score:
                            ticker_to_add = r
                            ticker_to_add_score = r_score
                    tickers.add(ticker_to_add)
                    remaining_tickers.remove(ticker_to_add)

                tickers = list(tickers)
                tickers_score = 0

                for i in range(N):
                    for j in range(i+1, N):
                        #print(corr_matrix[tickers[i]][tickers[j]])
                        tickers_score += corr_matrix[tickers[i]][tickers[j]]

                if tickers_score > highest_score:
                    highest = tickers
                    highest_score = tickers_score
                print('highest' + str(highest))
                print('highest score:' + str(highest_score))
            tickers = highest
        elif dataset_type == 'diversified':
            # Get all tickers
            all_tickers = list(table['Symbol'])

            # Remove banned tickers
            for t in banned_tickers:
                all_tickers.remove(t)

            # Convert dots to dashes in certain tickers
            for i in range(len(all_tickers)):
                if all_tickers[i] in convert_dot_to_dash_tickers:
                    all_tickers[i] = all_tickers[i].replace('.', '-')
                    # print(all_tickers[i])

            # The tickers' 1 year historical data is downloaded.
            period = '1mo'
            interval = '1d'
            data = yf.download(all_tickers, period=period,
                               interval=interval)['Adj Close']
            data = data.dropna()
            print('debug1:')
            null_tickers = []
            for t in all_tickers:
                if data[t].isnull().values.any():
                    print(data.pop(t))
                    null_tickers.append(t)
                elif data[t].empty:
                    print(data.pop(t))
                    null_tickers.append(t)

            # Remove banned tickers
            for t in null_tickers:
                all_tickers.remove(t)

            # The data is then processed to drop NaN values, then to calculate percent
            # change between months, and then to drop NaN values again.
            data = data.pct_change().dropna()

            # Mu is monthly expected return
            mu = data.mean(0)

            # Sigma is covariance between assets
            sigma = data.cov(0)

            # corr_matrix is correlation between assets
            corr_matrix = data.corr()

            highest = all_tickers[:N]
            highest_score = float('-inf')

            debugvar = 0
            for starting_ticker in all_tickers:
                debugvar += 1
                print('TRY ' + str(debugvar))
                remaining_tickers = list(all_tickers)
                tickers = set()
                tickers.add(starting_ticker)
                remaining_tickers.remove(starting_ticker)

                while(len(tickers) != N):
                    ticker_to_add = None
                    ticker_to_add_score = float('-inf')
                    
                    for r in remaining_tickers:
                        r_score = 0
                        for t in tickers:
                            r_score -= abs(corr_matrix[r][t])
                        if r_score > ticker_to_add_score:
                            ticker_to_add = r
                            ticker_to_add_score = r_score
                    tickers.add(ticker_to_add)
                    remaining_tickers.remove(ticker_to_add)

                tickers = list(tickers)
                tickers_score = 0

                for i in range(N):
                    for j in range(i+1, N):
                        #print(abs(corr_matrix[tickers[i]][tickers[j]]))
                        tickers_score -= abs(corr_matrix[tickers[i]][tickers[j]])

                if tickers_score > highest_score:
                    highest = tickers
                    highest_score = tickers_score
                print('highest' + str(highest))
                print('highest score:' + str(highest_score))
            tickers = highest

        print(tickers)
        print(len(tickers))

        for i in range(len(tickers)):
            if tickers[i] in convert_dot_to_dash_tickers:
                tickers[i] = tickers[i].replace('.', '-')
                print(tickers[i])

        print(str(N) + ' tickers used:')
        print(tickers)

        # The tickers' 1 year historical data is downloaded.
        period = '1mo'
        interval = '1d'
        data = yf.download(tickers, period=period,
                           interval=interval)['Adj Close']
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
