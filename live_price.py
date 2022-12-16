from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

# btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
# print(btc)

gh = cg.get_price(ids='bitcoin,fantom,ethereum', vs_currencies='usd,eur')
print(gh)


def get_price_token(token_name, pair):
    """get price of a token or Coin at the moment"""
    return cg.get_price(ids=token_name, vs_currencies=pair)


