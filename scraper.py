import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def safe_scraper():
    try:
        # Connect to AajTak with browser headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
        }
        
        response = requests.get('https://m.aajtak.in/', headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Working selectors (verified)
        articles = soup.select('div.story__detail')
        
        with open('news.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Title', 'Link'])
            
            for article in articles[:10]:
                title = article.select_one('h2').text.strip()
                link = article.find('a')['href']
                if not link.startswith('http'):
                    link = f'https://m.aajtak.in{link}'
                
                writer.writerow([
                    datetime.now().strftime("%H:%M"),
                    title,
                    link
                ])
                
    except Exception as e:
        print(f"ERROR: {str(e)}")
        with open('news.csv', 'w') as f:
            f.write("Time,Title,Link\n")
            f.write("00:00,Scraping Failed,https://error.com")

safe_scraper()
