import requests
from bs4 import BeautifulSoup
url = 'https://www.coingecko.com/id'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
result = []
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

headers_content = soup.find_all('div','gecko-table-container')
for content in headers_content:
    coin = content.find('a','tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between').text
    try:
        price = content.find('td','td-price price text-right pl-0').text
    except:
        continue
    try:
        volume_24H = content.find('td','td-liquidity_score').text
    except:
        continue
    try:
        volume_market = content.find('td','td-market_cap').text
    except:
        volume_market = 'Empty'

    final_data = {
        'Koin' : coin,
        'Harga' : price,
        'Volume 24 jam' : volume_24H,
        'Volume Market': volume_market,
    }

    result.append(final_data)
    for i in final_data:
        print(i)

