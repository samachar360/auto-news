import requests
from bs4 import BeautifulSoup
import csv
import datetime

# List of news websites to scrape
NEWS_SOURCES = [
    ('AajTak', 'https://www.aajtak.in/', '.story__title'),
    ('IndiaToday', 'https://www.indiatoday.in/', '.B1S3_title')
]

def auto_scrape():
    with open('news.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for source in NEWS_SOURCES:
            try:
                response = requests.get(source[1])
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.select(source[2])[:5]]
                
                for headline in headlines:
                    writer.writerow([
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        source[0],  # Website name
                        headline,
                        source[1]   # News URL
                    ])
            except Exception as e:
                print(f"Error in {source[0]}: {str(e)}")

if __name__ == "__main__":
    auto_scrape()
