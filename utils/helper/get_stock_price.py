import yfinance as yf


def get_stock_price(symbol:str):
    """
    Retrieve the most recent stock price data for a specified company using the Yahoo Finance API via the yfinance Python library.
    :param symbol: The stock symbol for which to retrieve data, e.g., 'NVDA' for Nvidia
    :output: A dictionary containing the most recent stock price data
    """
    
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval = "1m")
    latest = hist.iloc[-1]
    return {
        "timestamp": str(latest.name),
        "open": latest["Open"],
        "high": latest["High"],
        "low": latest["Low"],
        "close": latest["Close"],
        "volume": latest["Volume"]
    }
    
    