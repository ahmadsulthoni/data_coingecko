import os

import requests
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/id'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

result = []

res = requests.get(url, headers=headers)
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
content = soup.findAll('gecko-table-container')

try:
    os.mkdir('Hasil_data')
except FileExistsError:
    pass

#proses scraping
