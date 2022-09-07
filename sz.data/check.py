from util import *
import plotly.graph_objects as go
import plotly.express as px

# df = pd.read_pickle("sz.all.detail.df")
#
# df.to_excel("sz.detail.xlsx")


df = pd.read_excel("detail.0906.xlsx", index_col=0)
#
# # print boxplot
# df.turnover /= 1e8
# fig = px.box(df, y="turnover", points="all", log_y=True, notched=True)
# fig.show()
#
# exit(0)

# prev_close_price  last_price    outstanding_shares

gate100 = 10e8
gate99 = 3.45e8
gate75 = 1.56e8
gate50 = 0.676e8
gate25 = 0.3e8

df0 = df[df.turnover > gate100]
df1 = df[(gate100 >= df.turnover) & (df.turnover > gate99)]
df2 = df[(gate99 >= df.turnover) & (df.turnover > gate75)]
df3 = df[(gate75 >= df.turnover) & (df.turnover > gate50)]
df4 = df[(gate50 >= df.turnover) & (df.turnover > gate25)]
df5 = df[df.turnover <= gate25]


def ratio(df):
    print(df.shape[0], end=": ")
    prev = df.prev_close_price  # * df.outstanding_shares
    cur = df.last_price  # * df.outstanding_shares
    high = df.high_price  # * df.outstanding_shares
    low = df.low_price  # * df.outstanding_shares
    delta = (cur.sum() - prev.sum()) / prev.sum()
    delta1 = (high.sum() - prev.sum()) / prev.sum()
    delta2 = (low.sum() - prev.sum()) / prev.sum()
    return round(delta, 4), round(delta1, 4), round(delta2, 4)


#
print(ratio(df))
print(ratio(df0))
print(ratio(df1))
print(ratio(df2))
print(ratio(df3))
print(ratio(df4))
print(ratio(df5))

gate = [0, 10, 100, 500, 1500, 2500, 5000]
for i in range(1, len(gate)):
    s, e = gate[i - 1:i + 1]
    dff = df[s:e]
    print(s, e, ratio(dff))

# df.sort_values(by="turnover", ascending=True)
