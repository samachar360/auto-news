import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def live_scraper():
    try:
        # Connect to AajTak mobile news
        url = "https://m.aajtak.in/"
        response = requests.get(url, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Open CSV file to save news
        with open('news.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Title', 'Link'])  # Header
            
            # Find news articles
            for article in soup.select('div.story__card')[:10]:
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                if not link.startswith('http'):
                    link = f'{url}{link}'
                
                writer.writerow([
                    datetime.now().strftime("%H:%M"),
                    title,
                    link
                ])
                
    except Exception as e:
        print(f"Error: {str(e)}")

live_scraper()
