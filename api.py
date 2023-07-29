from collections import namedtuple
import requests

Coin = namedtuple('Coin',
                  'symbol name current_price market_cap_rank high_24h low_24h price_change_24h price_change_7d')


def get_crypto_data():
    base_url = "https://api.coingecko.com/api/v3/coins/markets"
    payload = {'vs_currency': 'eur',
               'order': 'market_cap_desc',
               'sparkline': 'false',
               'price_change_percentage': '24h,7d,30d'}

    data = requests.get(base_url, params=payload)
    json = data.json()

    coin_list = []

    for coin in json:
        symbol = coin['symbol']
        name = coin['name']
        current_price = '{:,}'.format(coin['current_price'])
        market_cap_rank = coin['market_cap_rank']
        high_24h = coin['high_24h']
        low_24h = coin['low_24h']
        price_change_24h = round(
            coin['price_change_percentage_24h_in_currency'], 2)
        price_change_7d = round(
            coin['price_change_percentage_7d_in_currency'], 2)

        current = Coin(symbol, name, current_price, market_cap_rank, high_24h, low_24h,
                       price_change_24h, price_change_7d)

        coin_list.append(current)

    return coin_list
