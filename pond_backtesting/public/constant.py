from enum import Enum


class Direction(Enum):
    """
    Direction of order/trade/position.
    """
    LONG = "多"
    SHORT = "空"
    NET = "净"


class Offset(Enum):
    """
    Offset of order/trade.
    """
    NONE = ""
    OPEN = "开"
    CLOSE = "平"
    CLOSETODAY = "平今"
    CLOSEYESTERDAY = "平昨"


class Exchange(Enum):
    """
    Exchange.
    """
    NONE = 'NONE'
    BITMEX = "BITMEX"
    HUOBI = "HUOBI"
    BITFINEX = "BITFINEX"
    BINANCE = "BINANCE"
    OKX = "OKX"
    BITGET = "BITGET"
    BYBIT = "BYBIT"
    COINBASE = "COINBASE"
    DERIBIT = "DERIBIT"
    GATEIO = "GATEIO"
    BITSTAMP = "BITSTAMP"
    DYDX = "DYDX"
    FTX = "FTX"


class Interval(Enum):
    """
    Interval of bar data.
    """
    TICK = "tick"
    MINUTE = "1m"
    HOUR = "1h"
    DAILY = "d"
    WEEKLY = "w"