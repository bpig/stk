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

    tgt = "0907"
    df.to_pickle("sz.data/detail.%s.df" % tgt)
