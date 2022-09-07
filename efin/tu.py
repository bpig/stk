import tushare as ts

ts.set_token("e50fc1ca00969fbd3d5247fbae4e1f6ae117f10537ce37440a686b5f")
pro = ts.pro_api()

df = pro.stock_basic(exchange='', list_status='L',
                     fields='ts_code,symbol,name,area,industry,market,list_date')
df.to_excel("sz.basic.xlsx")
