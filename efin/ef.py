import efinance as ef

# etf_code = ""
# df = ef.stock.get_quote_history(etf_code)


df = ef.stock.get_realtime_quotes()
df.to_parquet("0916.pq")
print(df)
#
