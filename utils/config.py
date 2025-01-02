tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather of a location with given latitude and longitude",
            "parameters": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "string",
                        "description": "The latitude of the location",
                    },
                    "long": {
                        "type": "string",
                        "description": "The longitude of the location",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit"
                    }
                },
                "required": ["lat", "long", "unit"]
            }
        }
    },
    
     {
        "type": "function",
        "function": {
            "name": "view_website",
            "description": "Return a markdown of a website with a given url",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The link of website",
                    },
                },
                "required": ["url"]
            }
        }
    },
     
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Retrieve the most recent stock price data for a specified company using the Yahoo Finance API via the yfinance Python library.\n:param symbol: The stock symbol for which to retrieve data, e.g.,  'NVDA' for Nvidia \n:output: A dictionary containing the most recent stock price data",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "title": "Symbol",
                    },
                },
                "required": ["symbol"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_symbol",
            "description": " Retrieve the stock symbol for a specified company using the Yahoo Finance API\n:param company: The name of the company for which to retrieve the stock symbol, e.g., 'Nvidia'.\n:output: The stock symbol for the specified company",
            "parameters": {
                "type": "object",
                "properties": {
                    "company": {
                        "type": "string",
                        "title": "Company",
                    },
                },
                "required": ["company"]
            }
        }
    },
]