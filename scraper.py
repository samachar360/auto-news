import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

NEWS_SOURCES = [
    {
        'name': 'AajTak',
        'url': 'https://www.aajtak.in/',
        'selector': 'div.story__card h2.story__title',
        'link_selector': 'div.story__card a'
    },
    {
        'name': 'Hindustan Times',
        'url': 'https://www.hindustantimes.com/',
        'selector': 'div.media-heading h3',
        'link_selector': 'div.media-heading a'
    },
    {
        'name': 'News18 India',
        'url': 'https://hindi.news18.com/',
        'selector': 'div.lead-mstory h2',
        'link_selector': 'div.lead-mstory a'
    }
]

def multi_source_scraper():
    with open('news.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Source', 'Title', 'Link'])  # Added Source column
        
        for source in NEWS_SOURCES:
            try:
                response = requests.get(source['url'], timeout=20)
                soup = BeautifulSoup(response.text, 'lxml')
                
                titles = [h.text.strip() for h in soup.select(source['selector'])]
                links = [a['href'] for a in soup.select(source['link_selector'])]
                
                for title, link in zip(titles[:10], links[:10]):
                    full_link = link if link.startswith('http') else source['url'] + link
                    writer.writerow([
                        datetime.now().strftime("%H:%M"),
                        source['name'],
                        title,
                        full_link
                    ])
                    
            except Exception as e:
                print(f"Error scraping {source['name']}: {str(e)}")
                continue

multi_source_scraper()
