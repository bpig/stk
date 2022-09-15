from util import *

# df = pd.read_excel("sz.basic.xlsx")

df = pd.read_excel("../sw_all.xlsx")
df = df[df['交易所'] == 'A股']
df["symbol"] = df["股票代码"].str.split(".", expand=True)[0].astype(np.int64)

df2 = pd.read_excel("../sz.data/detail.0908.xlsx", index_col=0)
cols = ['code', 'turnover', 'circular_market_val', 'net_profit']
df2 = df2[cols]

df2['symbol'] = df2.code.str.split(".", expand=True)[1].astype(np.int64)

dff = pd.merge(df, df2, on='symbol')

print(dff[:2])

dff.drop([df.columns[0], df.columns[1], 'symbol', '股票代码'], inplace=True, axis=1)

dff.set_index('公司简称', inplace=True)

print(dff[:2])
dff.to_excel("industry3.xlsx")
