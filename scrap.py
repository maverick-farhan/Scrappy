import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, folder):
    response = requests.get(url)
    filename = os.path.join(folder, url.split('/')[-1])
    
    with open(filename, 'wb') as file:
        file.write(response.content)

def scrape_website(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Download all PDFs
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            full_url = urljoin(url, href)
            print(f"Downloading PDF: {full_url}")
            download_file(full_url, folder)

    # If you want to scrape HTML content or other resources
    # Uncomment the line below
    with open(os.path.join(folder, 'index22.html'), 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == '__main__':
    website_url = 'http://www.example.com'  # Replace with the target website URL
    download_folder = 'downloaded_files'
    scrape_website(website_url, download_folder)
