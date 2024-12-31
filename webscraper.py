import requests
from bs4 import BeautifulSoup
import datetime

def scrape_news(stock_ticker, date):
    # Format the date for the query (e.g., 'YYYY-MM-DD')
    formatted_date = date.strftime('%Y-%m-%d')

    # Example: Use Google News (be sure to comply with their terms of service)
    query = f"{stock_ticker} stock {formatted_date}"
    url = f"https://www.google.com/search?q={query}&tbm=nws"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract news headlines and links
    articles = []
    for item in soup.select('div.dbsr'):  # CSS selector for news items
        title = item.select_one('div.JheGif').text
        link = item.a['href']
        articles.append({'title': title, 'link': link})

    return articles

# Test the scraper for a specific date
sample_date = datetime.datetime(2023, 11, 15)  # Replace with a date from your analysis
articles = scrape_news('AAPL', sample_date)
for article in articles:
    print(article['title'], "-", article['link'])
