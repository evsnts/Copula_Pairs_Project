'''
Import price data of S&P 500 companies form using the yfinance package.


'''
# insert needed libraries
import yfinance as yf
import requests
import bs4
import pandas as pd
class DataHandler:
    "Wrapper Class that imports data from yfinance."
    # -----------------------------------------------------------------
    def __init__(self):
        pass

    # -----------------------------------------------------------------
    def get_tickers(self):
        ''' Get the tickers of the S&P 500 companies.

        Returns:
        tickers(str, list) --  A list of the the S&P 500 companies' tickers.
        '''
        resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        table = soup.find('table', {'class': 'wikitable sortable'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)
        tickers = [s.replace('\n', '') for s in tickers]
        return tickers

    # -----------------------------------------------------------------
    def get_price_data(self, tickers, start, end, interval="5m"):
        '''Get the price data using a custom start and end date.

        Parameters:
        tickers (str, list) -- List of tickers.

        Returns:
        df(pandas dataframe) --- With the S&P 5000 companies price data.
        '''
        price_df = yf.download(tickers, start, end, interval=interval, group_by="column")["Close"]
        #price_df = price_df.iloc[1:]
        return price_df
    # -----------------------------------------------------------------
    def get_returns_data(self, price_df):
        '''Calculate return data with custom start and end date and interval.
        Parameters:
        price_df : pandas dataframe
            The price data
        Returns:
        returns_df: pandas dataframe
        The requested returns data.
        '''
        returns_df = price_df.pct_change()
        returns_df = returns_df.iloc[1:]
        return returns_df
