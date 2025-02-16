import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def simple_scraper():
    with open('news.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Source', 'Title', 'Link'])
        
        # Simple AajTak mobile scraper
        try:
            page = requests.get('https://m.aajtak.in/', timeout=10)
            soup = BeautifulSoup(page.text, 'lxml')
            
            for news in soup.find_all('div', class_='story__card')[:10]:
                title = news.find('h2').text.strip()
                link = news.find('a')['href']
                if not link.startswith('http'):
                    link = f'https://m.aajtak.in{link}'
                
                writer.writerow([
                    datetime.now().strftime("%d-%m %H:%M"),
                    "AajTak",
                    title,
                    link
                ])
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    simple_scraper()
