import requests
import json

from rich.traceback import install
install(show_locals=True)

def fetch_financial_news(api_token, stock_symbol, offset, limit):
    url = f"https://eodhistoricaldata.com/api/news?api_token={api_token}&s={stock_symbol}&offset={offset}&limit={limit}"
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Raise an exception for bad status codes
        news_data = response.json()
        return news_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except json.JSONDecodeError as json_err:
        print(f"JSON decoding error: {json_err}")
        return None

def display_news(news_data):
    if news_data is not None:
        for news_item in news_data:
            title = news_item["title"]
            description = news_item["content"]
            published_date = news_item["date"]
            news_url = news_item["link"]
            
            print(f"Title: {title}")
            print(f"Published Date: {published_date}")
            print(f"Description: {description}")
            print(f"URL: {news_url}")
            print("-" * 40)  # Separator between news items
    else:
        print("No news data available.")

def main():
    api_token = "649954668f1d54.62736115"
    stock_symbol = "AAPL.US"
    offset = 0
    limit = 10

    news_data = fetch_financial_news(api_token, stock_symbol, offset, limit)
    display_news(news_data)

if __name__ == "__main__":
    main()
