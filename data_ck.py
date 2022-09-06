import pandas as pd
from futu import *
from util import *

df = pd.read_excel("sz.20220905.xlsx", index_col=0)
print(type(df))
print(df.columns)
print(df.index[:3])
print(df.code[:3].to_list())
