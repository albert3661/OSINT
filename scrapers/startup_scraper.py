import requests
from bs4 import BeautifulSoup
from .utils import clean_text

def scrape_startup_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = clean_text(soup.find('h1', class_='startup-name'))
        description = clean_text(soup.find('p', class_='startup-description'))
        funding = clean_text(soup.find('div', class_='startup-funding'))
        partners = [clean_text(p) for p in soup.find_all('ul', class_='startup-partners')]
        return {'name': name, 'description': description, 'funding': funding, 'partners': partners}
    else:
        print('Failed to fetch startup info:', response.status_code)
        return None
