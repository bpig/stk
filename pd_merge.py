from futu import *
from logger import *

df1 = pd.read_pickle('sz.all2.df')

df1.total_market_val = df1.total_market_val / 1e+9

ans = None

with Connect() as ctx:
    ct = df1.shape[0]
    for i in range(0, ct, 400):
        print(i, time.ctime())
        sub = df1[i:i + 400]
        # print(sub.index.to_list())
        codes = sub.code.to_list()
        ret, data = ctx.get_market_snapshot(codes)
        if ret == RET_OK:
            data.index = sub.index
            ans = pd.concat([ans, data])

ans.to_pickle("sz.all.detail.df")
ans.to_csv("sz.all.detail2.csv", encoding='utf-8')
# print(df1[['code', 'total_market_val']])
