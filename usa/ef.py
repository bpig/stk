import efinance as ef

# etf_code = ""
# df = ef.stock.get_quote_history(etf_code)


df = ef.stock.get_realtime_quotes("美股")
df.to_excel("usa_0914.xlsx")
#
