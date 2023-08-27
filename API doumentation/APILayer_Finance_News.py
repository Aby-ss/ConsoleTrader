import requests

url = "https://api.apilayer.com/financelayer/news?apikey=EHw0Ndjb26EG0xvAK5uNSO5oNkgp5w73&tickers=appl&tickers=btc&tags=Oil&sources=forbes.com&sort=desc&offset=5&limit=5&keywords=oil%20prices&fallback=on&date=thismonth"

payload = {}

response = requests.request("GET", url, data=payload)

status_code = response.status_code
result = response.text

print("Response Status Code:", status_code)
print("Response Content:")
print(result)
