import plotly.express as px
import plotly.graph_objects as go
from util import *

df = pd.read_excel("industry2.xlsx", index_col=0)
df.net_profit /= 1e8
df.turnover /= 1e8

for key in ['银行', '保险', '电信运营', '石油开采', '水运', '石油加工']:
    df = df[df.industry != key]

fig = go.Figure()
# fig.add_trace(go.Box(x=df.industry, y=df.net_profit))
# fig.add_trace(go.Box(x=df.industry, y=df.turnover))


fig.add_trace(go.Box(y=df.industry, x=df.net_profit, name='net_profit'))
fig.add_trace(go.Box(y=df.industry, x=df.turnover, name='turnover'))

fig.update_layout(
    yaxis_title='lee&nn',
    boxmode='group'  # group together boxes of the different traces for each value of x
)
fig.update_traces(orientation='h')
fig.show()
# fig = px.box(df, x='industry', y='net_profit')
# fig.show()
