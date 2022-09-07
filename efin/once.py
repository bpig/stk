from util import *

df = pd.read_excel("sz.basic.xlsx")

df2 = pd.read_excel("../sz.data/detail.0907.xlsx", index_col=0)
cols = ['code', 'turnover', 'circular_market_val', 'net_profit']
df2 = df2[cols]
df2['symbol'] = df2.code.str.split(".", expand=True)[1].astype(np.int64)

dff = pd.merge(df, df2, on='symbol')

print(dff[:2])

dff.to_excel("industry.xlsx")
