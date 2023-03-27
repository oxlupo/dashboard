from pycoingecko import CoinGeckoAPI
import pandas as pd

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

