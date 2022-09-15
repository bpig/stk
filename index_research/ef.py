import efinance as ef
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis


# df = ef.stock.get_daily_billboard()
# df.to_excel("tiger.xlsx")


# 000001  上证指数

etf = "000001", "上证指数"
# etf = "399001", "深证成数"
etf = "399006", "创业板指"

etf = "宁德时代", "宁德时代"
etf = "600795", "国电电力"
df = ef.stock.get_quote_history(etf[1])

df.to_excel(etf[1] + ".xlsx")

exit(1)
df = pd.read_excel(etf[0] + ".xlsx", index_col=0)
df = df[-50:]

x = list(range(df["日期"].shape[0]))
k0 = df["开盘"]
k1 = df["收盘"]
k2 = df["最高"]
k3 = df["最低"]

money = df["成交额"]

# fig = go.Figure()
# fig = make_subplots(specs=[[{"secondary_y": True}]])
fig = make_subplots(rows=2, cols=1,  row_heights=[0.8, 0.2])

fig.add_trace(go.Scatter(x=x, y=k0, mode='lines+markers', name='开盘'))
fig.add_trace(go.Scatter(x=x, y=k1, mode='lines+markers', name='收盘'))
fig.add_trace(go.Scatter(x=x, y=k2, mode='lines+markers', name='最高'))
fig.add_trace(go.Scatter(x=x, y=k3, mode='lines+markers', name='最低'))

# fig.add_trace(go.Bar(x=x, y=money, name="turnover"), secondary_y=True)
fig.add_trace(go.Bar(x=x, y=money, name="turnover"), row=2, col=1)

fig.show()

# fig = px.box(df, x='industry', y='net_profit')
# fig.show()

# df = ef.stock.get_realtime_quotes('ETF')
# df.to_excel("etf.xlsx")
#
