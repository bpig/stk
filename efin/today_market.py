import pandas as pd
from datetime import date
from pathlib import Path
import efinance as ef
import os
import warnings
warnings.filterwarnings(
    "ignore", message=".*notifyAll.*", category=DeprecationWarning
)


def get_today(today=None):
    if today is None:
        today = str(date.today())
    fname = f"daily/{today}.pq"
    if os.path.exists(fname):
        print(f"read cached {fname}")
        return pd.read_parquet(fname)

    df = ef.stock.get_realtime_quotes()
    # for new column map
    ori_columns = ['股票代码', '股票名称', '涨跌幅',
                   '最新价', '最高', '最低', '今开',
                   '涨跌额', '换手率', '量比', '动态市盈率',
                   '成交量', '成交额', '昨日收盘', '总市值', '流通市值',
                   '行情ID', '市场类型', '更新时间', '最新交易日']
    columns = ['code', 'name', 'ratio', 'price', 'high', 'low', 'open',
               'changed', 'turnover', 'vr', 'dpe',
               'volume', 'amount', 'p_price', 'cap', 'traded_cap',
               'unknown', 'market', 'updated', 'date']
    df.columns = columns

    keys = ['code', 'name', 'ratio','turnover','amount','volume_ratio',
            'price', 'prev_price', 'open', 'high', 'low', 'changed',
            'dpe', 'volume',  'cap', 'traded_cap', 'market', 'date']
    sub = df[keys]
    # ignore stopped stock
    sub = sub.query('amount != "-"')
    sub = sub.infer_objects()
    # dump today
    sub.to_parquet(f"{fname}")
    return sub

def get_one(stock):
    """stock: code or name"""
    df = ef.stock.get_quote_history(stock)
    ori_columns = ['股票名称', '股票代码', '日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅',
       '涨跌额', '换手率']
    columns = ['name', 'code', 'date', 'open', 'close', 'high', 'low', 'volume', 'amount', 'amplitude', 'ratio',
               'changed', 'turnover']
    df.columns = columns
    fname = f"one/{stock}.pq"
    sub = df.infer_objects()
    sub.to_parquet(f"{fname}")
    return sub





