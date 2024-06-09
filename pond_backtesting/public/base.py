import re

# 数据库名称
TICK_DB_NAME = 'VnTrader_Tick_Db'
DAILY_DB_NAME = 'VnTrader_Daily_Db'
MINUTE_DB_NAME = 'VnTrader_1Min_Db'
HOUR_DB_NAME = 'VnTrader_1Hour_Db'

def MinuteDataBaseName(duration:int):
    return re.sub("\d", f'{duration}', MINUTE_DB_NAME)

def HourDataBaseName(duration:int):
    return re.sub("\d", f'{duration}', HOUR_DB_NAME)
