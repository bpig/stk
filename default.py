import pandas as pd
from futu import *

df = pd.DataFrame(columns=['code', 'category', 'list_time'])

for line in open("default.log"):
    line = line.strip()
    if "==" in line or not line:
        continue
    items = line.split()
    if len(items) == 2:
        category = items[0]
    elif len(items) == 3:
        continue
    else:
        _, code, name, list_time = items
        df.loc[name] = [code, category, list_time]

df.to_excel("sz.category.xlsx")
