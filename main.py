import yfinance as yf
import pandas as pd
import time

def read_portfolio(csv):
    """
    Read in a local csv file and create a list of tickers for submission to Yfinance API
    Return: ticker_list
    """
    portfolio = pd.read_csv(f"./{csv}.csv", index_col=0)
    ticker_list = []
    for index, row in portfolio.iterrows():
        ticker_list.append(row["ticker"])
    return ticker_list, portfolio

def get_stock_price(tickerlist):
    '''
    Takes a list of tickers and fetches the price of each stock from the Yfinance API
    Return: a Pandas dataframe with the ticker as the index and the price in the column
    '''
    price = yf.download(tickerlist, threads=True, period='1d', interval="1d")
    price_df = price['Adj Close']
    price_df = price_df.transpose()
    price_df.columns = ['price', 'price1']
    return price_df

def get_stock_dividend(tickerlist):
    '''
    Get the annual dividend from Yfinance
    Return: a Pandas dataframe with the ticker as the index and the dividend in the column
    '''
    dividend_dict = dict()
    for ticker in tickerlist:
        price = yf.Ticker(ticker)
        dividend_dict[ticker] = price.info['dividendRate']
    dividend_df = pd.DataFrame.from_dict(dividend_dict,orient='index', columns=['dividend'])
    return dividend_df

def construct_dataframe(portfolio = None, price_data = None, dividend_data = None):
    '''
    Create the final dataframe to record the new stock price and calculate profit
    Return: a Pandas dataframe with the final values
    '''
    frames = [portfolio, price_data, dividend_data]
    final_df = pd.concat(frames, axis=1)
    final_df = final_df.rename(columns={'price':'currentPrice'})
    final_df = final_df.drop(['price1'], axis=1)
    #create a new column with the new value of the stock
    final_df = final_df.fillna(0)
    final_df['value'] = final_df['quantity'].multiply(final_df['currentPrice'])
    final_df['newValue'] = final_df['value'].add(final_df['dividend'])
    final_df['profit%'] = final_df['value'].divide(final_df['purchaseValue'])

    total = final_df.sum(axis=0)
    new_value = int(total['newValue'])
    current_value = int(total['currentValue'])
    profit = new_value - current_value

    new_df = final_df.drop(['purchaseValue', 'purchasePrice', 'currentValue'], axis=1)

    def style_df_negative(val):
        '''Helper function to change negative numbers red
        IN PROGRESS'''
        colour = 'red' if val < 1 else 'Black'
        return 'colour: %s' % colour

    new_df.style.format({"profit%": "{:.1%}"}) #figure out how to display the different as a %
    # , subset=['profit%']       
    # new_df = new_df.style.applyy(style_df_negative, subset=['profit%'])

    return new_df, profit

def dashboard(profit, final_df):
    """TODO: Dashboard logic to go here"""
    profit = profit

    return None

# Start of main function

start = time.perf_counter() #start a performance timer

ticker_list = []
ticker_list, portfolio_df = read_portfolio("portfolio")
price_df = get_stock_price(ticker_list)
dividend_df = get_stock_dividend(ticker_list)
final_df, profit = construct_dataframe(portfolio_df, price_df, dividend_df)

##########PRINT DEUBBING##########
print(final_df)
print(profit)
##################################

finish = time.perf_counter()
print(finish - start) #time program execution time

"""
TODO: sys arguments for whether to find price or dividdend or both?
TODO: dashboard, biggest winner, biggest loser, total profit?
TODO: tax?
TODO: output to CSV
"""