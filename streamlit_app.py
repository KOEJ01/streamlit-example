import yfinance as yf
import datetime as dt

# Set the stock symbol and the strike price
symbol = 'SPY'
strike_price = 150

# Set the start and end dates
start_date = dt.datetime.today()
end_date = start_date + dt.timedelta(days=365)

# Get the options data for the specified stock and strike price
options = yf.Ticker(symbol).option_chain(date=start_date.strftime('%Y-%m-%d'))
calls = options.calls[options.calls['strike']==strike_price]

# Loop through each expiration date in the next 12 months and get the options data
for i in range(12):
    expiration_date = start_date.replace(day=1) + dt.timedelta(days=31) - dt.timedelta(days=1)
    options = yf.Ticker(symbol).option_chain(date=expiration_date.strftime('%Y-%m-%d'))
    calls = options.calls[options.calls['strike']==strike_price]
    print('Options data for expiration date:', expiration_date.strftime('%Y-%m-%d'))
    print(calls)
    start_date = expiration_date + dt.timedelta(days=1)
