import yfinance as yf
import numpy as np

def get_data(tickers, period, interval):
    # Download data
    data = yf.download(tickers, period=period, interval=interval)['Adj Close']
    return data

def get_sigma_and_mu_from_tickers(data):
    # Mu is monthly expected return multiplied by twelve months
    mu = data.pct_change().mean(0)

    # Sigma is covariance between assets
    sigma = data.pct_change().cov(0)

    return (sigma, mu)