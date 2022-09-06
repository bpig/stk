from logger import *

df = pd.read_pickle("sz.all.detail.df")

df.to_excel("sz.detail.xlsx")
