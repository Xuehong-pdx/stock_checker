import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz


def check_symbol(symbol):
    ticker = yf.Ticker(symbol)
    if ticker:
        return True
    else:
        print(f'{symbol.upper()} is not a valid symbol.')


def get_ticker_info(ticker):
    t = yf.Ticker(ticker)
    # df = t.history('max')
    # df = df.reset_index()
    try:
        close_price = round(t.info['previousClose'], 2) 
        open_price = round(t.info['regularMarketOpen'], 2) 
        high = round(t.info['regularMarketDayHigh'], 2) 
        low = round(t.info['regularMarketDayLow'], 2) 
        return ticker, close_price, open_price, high, low
    except:
        return None, None, None, None, None


def get_stocks(symbols, timezone='America/Denver'):
    stock_values = []
    for symbol in symbols:
        ticker = symbol.upper().strip()
        if check_symbol(ticker) == True:
            ticker, close_price, open_price, high, low = get_ticker_info(ticker)
            if ticker and close_price and open_price and high and low:
                stock_values.append([ticker, close_price, open_price, high, low, low-close_price])

    if not stock_values:
        return None, None

    df = pd.DataFrame(stock_values, columns = ['symbol', 'Previous_close', 'Current_open', 'high', 'low', 'change'])
    df['change'] = df.change.apply(lambda x: round(x, 2))
    df['change%'] = round(df.change / df.Previous_close *100, 2)
    timezone = pytz.timezone(timezone)

    return df, datetime.now(timezone)


def check_stocks(timezone='America/Denver'):
    '''
    sample run from container shell: python3 -c 'from functions import check_stocks; check_stocks()'
    '''
    symbols = input('Enter your stock symbols - separate by space: ')
    if not symbols:
        symbols = '^DJI AAPL GOOG GC=F TSLA'
    symbols = [str(x) for x in symbols.split()]
    
    df, localtime = get_stocks(symbols, timezone)
    print(f'Here is the stock infor as of {localtime}')
    print(df)
