import requests

def get_symbol(company:str) -> str:
    """
    Retrieve the stock symbol for a specified company using the Yahoo Finance API
    :param company: The name of the company for which to retrieve the stock symbol, e.g., 'Nvidia'.
    :output: The stock symbol for the specified company
    """
    
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": company, "country": "United States"}
    user_agents = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    
    res = requests.get(url, params, headers=user_agents)
    
    data = res.json()
    symbol = data['quotes'][0]['symbol']
    
    return symbol
    