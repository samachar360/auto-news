import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def safe_scraper():
    try:
        # Get mobile-friendly AajTak page
        response = requests.get('https://m.aajtak.in/')
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Create CSV file with headers
        with open('news.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'Title', 'Link'])
            
            # Simple mobile selector
            for article in soup.select('div.story__card')[:5]:
                title = article.find('h2').text.strip()
                link = article.find('a')['href']
                if not link.startswith('http'):
                    link = f'https://m.aajtak.in{link}'
                
                writer.writerow([
                    datetime.now().strftime("%H:%M"),
                    title,
                    link
                ])
                
    except Exception as e:
        print(f"Error: {str(e)}")

safe_scraper()
