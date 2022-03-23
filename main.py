import requests
from bs4 import BeautifulSoup
url = 'https://www.coingecko.com/id'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

headers_content = soup.find_all('div','tw-flex tw-items-center')
print(headers_content)