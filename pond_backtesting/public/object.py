"""
Basic data structure used for general trading function in VN Trader.
"""

from dataclasses import dataclass
from datetime import datetime
from .constant import Exchange, Interval
import numpy as np
from copy import copy


@dataclass
class BaseData:
    """
    Any data object needs a gateway_name as source
    and should inherit base data.
    """

    gateway_name: str


@dataclass
class TickData(BaseData):
    """
    Tick data contains information about:
        * last trade in market
        * orderbook snapshot
        * intraday market statistics.
    """

    symbol: str
    exchange: Exchange
    datetime: datetime

    name: str = ""
    volume: float = 0
    turnover: float = 0
    open_interest: float = 0
    last_price: float = 0
    last_volume: float = 0
    limit_up: float = 0
    limit_down: float = 0

    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    pre_close: float = 0

    bid_price_1: float = 0
    bid_price_2: float = 0
    bid_price_3: float = 0
    bid_price_4: float = 0
    bid_price_5: float = 0

    ask_price_1: float = 0
    ask_price_2: float = 0
    ask_price_3: float = 0
    ask_price_4: float = 0
    ask_price_5: float = 0

    bid_volume_1: float = 0
    bid_volume_2: float = 0
    bid_volume_3: float = 0
    bid_volume_4: float = 0
    bid_volume_5: float = 0

    ask_volume_1: float = 0
    ask_volume_2: float = 0
    ask_volume_3: float = 0
    ask_volume_4: float = 0
    ask_volume_5: float = 0

    localtime: datetime = None

    def __post_init__(self):
        # 增加了if判断
        if self.exchange:
            self.vt_symbol = f"{self.symbol}.{self.exchange.value}"
        else:
            self.vt_symbol = self.symbol


@dataclass
class BarData(BaseData):
    """
    Candlestick bar data of a certain trading period.
    """

    symbol: str
    exchange: Exchange
    datetime: datetime
    endDatetime: datetime = None  # bar结束datetime

    interval: Interval = None
    volume: float = 0
    turnover: float = 0
    open_interest: float = 0
    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0

    def __post_init__(self):
        if self.exchange:
            self.vt_symbol = f"{self.symbol}.{self.exchange.value}"
        else:
            self.vt_symbol = self.symbol

    def check_valid(self):
        if self.open_price == 0 or self.high_price == 0 or self.low_price == 0 or self.close_price == 0:
            return False

        if np.isnan(self.open_price) or np.isnan(self.high_price) or np.isnan(self.low_price) or np.isnan(self.close_price):
            return False

        return True

    def merge_data(self, old_data:dict):
        new_data = copy(old_data)
        merge_dict = {'open':'open_price',
                      'high':'high_price',
                      'low':'low_price',
                      'close':'close_price',
                      'gatewayName':'gateway_name',
                      'openInterest':'open_interest',
                      'vtSymbol':'vt_symbol'}
        for key, value in merge_dict.items():
            if key in new_data:
                new_data[value] = new_data.pop(key)
        return new_data
