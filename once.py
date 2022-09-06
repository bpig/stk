import pandas as pd
from futu import *
from util import *

df0 = pd.read_excel("sz.category.xlsx", index_col=0)
df1 = pd.read_excel("sz.data/detail.0906.xlsx", index_col=0)

print(df0.shape[0])

df1 = df1[['code', 'total_market_val']]
df = pd.merge(df0, df1, how="inner", on=['code'])
df.index = df0.index

print(df[:1])
df.to_excel("category.detail.xlsx")
