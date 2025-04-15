import pandas as pd
from datetime import date
from pathlib import Path
import efinance as ef
import os
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

    keys = ['code', 'name', 'ratio','turnover','amount','vr',
            'price', 'p_price', 'open', 'high', 'low', 'changed',
            'dpe', 'volume',  'cap', 'traded_cap', 'market', 'date']
    sub = df[keys]
    # ignore stopped stock
    sub = sub.query('amount != "-" and vr != "-"')
    sub = sub.infer_objects()
    # dump today
    sub.to_parquet(f"{fname}")
    return sub

def get_one(stock, load=False):
    """stock: code or name"""
    fname = f"one/{stock}.pq"
    if load:
        df = pd.read_parquet(fname)
        return df
    df = ef.stock.get_quote_history(stock)
    ori_columns = ['股票名称', '股票代码', '日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅',
       '涨跌额', '换手率']
    columns = ['name', 'code', 'date', 'open', 'close', 'high', 'low', 'volume', 'amount', 'amplitude', 'ratio',
               'changed', 'turnover']
    df.columns = columns

    sub = df.infer_objects()
    sub.to_parquet(f"{fname}")
    return sub

def andy_indicator(df, date=None):
    if date:
        df = df.query(f'date > "{date}"').reset_index(drop=True)
    df['e13'] = ta.ema(df.close, 13)
    df['e21'] = ta.ema(df.close, 21)
    df['e70'] = ta.ema(df.close, 70)
    df['e84'] = ta.ema(df.close, 84)
    df['fast'] = df[['e21', 'e13']].min(axis=1)
    df['slow'] = df[['e70', 'e84']].max(axis=1)
    df['gap'] = df['fast'] / df['slow'] - 1
    df['slope'] = df.gap.diff(1)
    return df

def plot(df, second=False, window=5):
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.update_layout(
        width=1000,
        height=600,
    )
    fig.update_xaxes(type='category')
    fig.add_trace(
        go.Scatter(
            x=df.date,
            y=df.gap,
            mode='lines+markers',
            name='gap'
        ),
        secondary_y=False
    )
    if second:
        fig.add_trace(
            go.Scatter(
                x=df.date,
                y=df.segment,
                mode='lines+markers',
                name='slope'
            ),
            secondary_y=True
        )
        # fig.add_trace(
        #     go.Scatter(
        #         x=df.date,
        #         y=df.slope.rolling(window, center=True).mean(),
        #         mode='lines+markers',
        #         name='smooth'
        #     ),
        #     secondary_y=True
        # )
    fig.show()




