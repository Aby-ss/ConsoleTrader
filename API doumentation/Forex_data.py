import requests

# Define your Fixer API access key
API_KEY = '28228f79520824b0239d5db15ef61022'
API_ENDPOINT = f'http://data.fixer.io/api/latest?access_key={API_KEY}'

def fetch_forex_data():
    try:
        response = requests.get(API_ENDPOINT)
        data = response.json()

        if 'error' in data:
            return f"Error: {data['error']['type']} - {data['error']['info']}"
        else:
            base_currency = data['base']
            date = data['date']
            exchange_rates = data['rates']

            result = f"Base Currency: {base_currency}\nDate: {date}\n\nExchange Rates:\n"
            for currency, rate in exchange_rates.items():
                result += f"{currency}: {rate}\n"
            
            return result
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

if __name__ == "__main__":
    forex_data = fetch_forex_data()
    print(forex_data)
