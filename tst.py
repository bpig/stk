import sys
import pprint

from futu import *
from logger import Logger

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_pickle("A.2022_0905.all")

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

logger = Logger()
ct = df.shape[0]
for c in range(ct):
    s = df.iloc[c]
    ret, data = quote_ctx.get_plate_stock(s.code)
    if ret == RET_OK:
        stks = data['stock_name'].values.tolist()
        print(s.plate_name, len(stks))
        # pprint.pprint(stks)
        print(data[['code', 'stock_name', 'list_time']])
        print("=" * 100)
    else:
        print('error:', data)
    logger.flush()
    time.sleep(3)

quote_ctx.close()
# print(df)

# print(df.columns.values)
