import requests
from rich import print, box
from rich.panel import Panel
from rich.layout import Layout
from rich.traceback import install
install(show_locals=True)

url = "https://api.apilayer.com/financelayer/news?apikey=EHw0Ndjb26EG0xvAK5uNSO5oNkgp5w73&tickers=appl&tickers=btc&tags=Oil&sources=forbes.com&sort=desc&offset=5&limit=5&keywords=oil%20prices&fallback=on&date=thismonth"

response = requests.get(url)
data = response.json()

news_objects = data["data"]

for news in news_objects:
    title = news["title"]
    description = news["description"]
    url = news["url"]
    source = news["source"]
    published_at = news["published_at"]
    
    panel = Panel(
        
        f"Description: {description}\n"
        f"Source: {source}\n"
        f"Published At: {published_at}",
        title=f"[link={url}]Title:[/link] {title}\n",
        title_align="left",
        border_style="bold white",
        box=box.SQUARE
    )
    
    print(panel)
    print()  # Add an empty line between panels
