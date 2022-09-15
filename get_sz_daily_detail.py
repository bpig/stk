from futu import *
from util import *

sz = pd.read_excel("sz.20220905.xlsx", index_col=0)
ct = sz.shape[0]
print(ct)

df = None

with Connect() as conn:
    for i in range(0, ct, 400):
        sz_ = sz[i:i + 400]
        codes = sz_.code.to_list()
        names = sz_.index
        ret, data = conn.get_market_snapshot(codes)
        if ret != RET_OK:
            print("error:", i, data)
            break
        data.index = names
        df = pd.concat([df, data])

    tgt = "0909"
    columns = ['code', 'update_time', 'listing_date',
               'prev_close_price', 'last_price', 'open_price', 'high_price', 'low_price',
               'volume', 'turnover', 'circular_market_val', 'net_profit', 'turnover_rate', 'amplitude',
               'avg_price', 'bid_ask_ratio', 'volume_ratio',
               'highest52weeks_price', 'lowest52weeks_price',
               'highest_history_price', 'lowest_history_price', 'close_price_5min',
               'issued_shares', 'total_market_val', 'net_asset',
               'earning_per_share',
               'outstanding_shares', 'net_asset_per_share', 'ey_ratio', 'pe_ratio', 'pb_ratio',
               'pe_ttm_ratio', 'dividend_ttm', 'dividend_ratio_ttm', ]

    df = df[columns]
    df.to_excel("sz.data/detail.%s.xlsx" % tgt)
