import efinance as ef

df = ef.stock.get_realtime_quotes()
df.to_excel("0907.xlsx")
