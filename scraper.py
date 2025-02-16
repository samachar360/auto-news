import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def safe_scraper():
    try:
        # Get AajTak mobile site
        url = "https://m.aajtak.in/"
        response = requests.get(url, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        with open('news.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Title', 'Link'])
            
            # Working mobile selector
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
        print(f"ERROR: {str(e)}")

safe_scraper()
