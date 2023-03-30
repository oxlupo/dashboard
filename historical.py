from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
cg = CoinGeckoAPI()


def get_price_token(token_name, pair):
    """get price of a token or Coin at the moment"""
    if not isinstance(token_name, dict):

        return cg.get_price(ids=token_name, vs_currencies=pair)
    else:
        raise Exception("An Error was occur don't use Dict for token_list")


def dataframe_coin():
    """all tokens and coin in table:return"""

    coin_list = cg.get_coins_list()
    coin_df = pd.DataFrame.from_dict(coin_list).sort_values("id").reset_index(drop=True)
    return coin_df


def get_historical_data(id: str, days: str, interval: str, vs_currency: str):
    """
    id='bitcoin'
    days= '150'
    interval= 'daily'
    vs_currency= 'usd'
    """

    try:
        token_hist = cg.get_coin_market_chart_by_id(id=id, vs_currency=vs_currency, days=days, interval=interval)["prices"]
        historical_list = list(map(lambda index: index[1], token_hist))
        return historical_list
    except Exception as e:
        print(e)


def several_historical_data(token_list: list, days: str):
    """
    token_list -> ["bitcoin", "ethereum", "fantom", "link", "litecoin"]:param
    """
    historical_dict = dict()
    try:
        for token in token_list:
            hist = get_historical_data(id=token, days=days, interval="daily", vs_currency="usd")
            if not hist == None:

                historical_dict[token] = hist
        hist_df = pd.DataFrame(historical_dict)
    except Exception as e:
        print(e)

    return hist_df


def token_returns(token, days: str):
    """get return of each token in a dataframe"""
    if isinstance(token, pd.DataFrame):
        return_df = token.pct_change(1).dropna()

        return return_df

    if isinstance(token, str):
        returns = get_historical_data(id=token, days=days, interval="daily", vs_currency='usd')

        return returns




token_list = ["bitcoin", "ethereum", "fantom", "link", "litecoin"]
