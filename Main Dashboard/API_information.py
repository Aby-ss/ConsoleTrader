import requests

# Your Alpha Vantage API key
api_key = "78H5RH2BRNG4G5Z6"

def get_data(function, symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def retrieve_forex_rates(currencies):
    forex_rates = {}
    for currency in currencies:
        forex_data = get_data("CURRENCY_EXCHANGE_RATE", f"USD/{currency}")
        forex_rates[currency] = {
            "Exchange Rate": forex_data.get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate", None),
            "Last Refreshed": forex_data.get("Realtime Currency Exchange Rate", {}).get("6. Last Refreshed", None)
        }
    return forex_rates

def retrieve_crypto_data(cryptos):
    crypto_data = {}
    for crypto in cryptos:
        crypto_intraday_data = get_data("DIGITAL_CURRENCY_INTRADAY", f"{crypto}/USD")
        time_series = crypto_intraday_data.get("Time Series Crypto (5min)", {})
        if time_series:
            last_refreshed = list(time_series.keys())[-1]
            crypto_data[crypto] = {
                "Last Refreshed": last_refreshed,
                "Price": time_series[last_refreshed].get("1a. price (USD)", None)
            }
        else:
            crypto_data[crypto] = {
                "Last Refreshed": None,
                "Price": None
            }
    return crypto_data

def retrieve_economic_data(indicators):
    economic_data = {}
    for indicator in indicators:
        economic_data[indicator] = get_data("ECONOMIC_INDICATOR", indicator)
    return economic_data

def retrieve_commodities_data(commodities):
    commodities_data = {}
    for commodity in commodities:
        commodities_data[commodity] = get_data("TIME_SERIES_INTRADAY", f"{commodity}/USD")
    return commodities_data

# List of variables to cycle through
currencies_list = ["EUR", "JPY", "GBP"]
cryptos_list = ["BTC", "ETH"]
economic_indicators_list = ["GDP", "TREASURY_YIELD", "INFLATION", "RETAIL_SALES", "UNEMPLOYMENT_RATE"]
commodities_list = ["GOLD", "SILVER", "OIL"]

# Retrieve data using functions
forex_data = retrieve_forex_rates(currencies_list)
crypto_data = retrieve_crypto_data(cryptos_list)
economic_data = retrieve_economic_data(economic_indicators_list)
commodities_data = retrieve_commodities_data(commodities_list)

# Display retrieved data
print("Forex Data:")
print(forex_data)

print("Crypto Data:")
print(crypto_data)

print("Economic Data:")
print(economic_data)

print("Commodities Data:")
print(commodities_data)