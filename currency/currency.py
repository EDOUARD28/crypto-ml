import pandas as pd
import yfinance as yf


class CURRENCY:

    LINK_CRYPTO_CURRENCY_INDEX = {
        "bitcoin": "BTC",
        "ethereum": "ETH",
        "binance": "BNB",
        "tether": "USDT",



    }

    CURRENCIES_LIST = (
        ("USD", "US Dollard")
    )

    def __init__(
            self,
            name,
    ):
        self.name = name

    @property
    def _index(self):
        return self.LINK_CRYPTO_CURRENCY_INDEX.get(self.name)

    def print_possible_currencies(self):
        print(self.CURRENCIES_LIST)

    def get_historical_data(self, period: str = "12mo", interval: str = "15m", currency: str = "USD") -> pd.DataFrame:
        return yf.download(
            tickers=f'{self._index}-{currency}',
            period=period,
            interval=interval
        )
