# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

from futu import *

cols = set()
with open("default.log") as d:
    for l in d:
        if "SZ" in l or "SH" in l:
            d, n = l.split()[1:3]
            v = d + '_' + n
            # v = d
            cols.add(v)

import pprint

pprint.pp(cols)
cols = list(cols)
ct = len(cols)

df = None

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # 创建行情对象
for i in range(0, ct, 400):
    codes = cols[i:i + 400]
    codes, names = zip(*map(lambda x: x.split("_"), codes))
    print(codes)
    print(names)

    ret, data = quote_ctx.get_market_snapshot(list(codes))
    if ret != RET_OK:
        print("error:", i, data)
        break
    data.index = names
    df = pd.concat([df, data])


df.to_pickle("sz.all2.df")
quote_ctx.close()

# # df = quote_ctx.get_market_snapshot('HK.00700')  # 获取港股 HK.00700 的快照数据
# # print(df)
# # df[1].to_pickle("007.df")
#
#
# ret, df = quote_ctx.get_plate_list(Market.SH, Plate.ALL)
#
# if ret == RET_OK:
#     df.to_pickle("A.2022_0905.all")
# else:
#     print("error:", df)
#
# quote_ctx.close()  # 关闭对象，防止连接条数用尽

# trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)  # 创建交易对象
# print(trd_ctx.place_order(price=500.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY,
#                          trd_env=TrdEnv.SIMULATE))  # 模拟交易，下单（如果是真实环境交易，在此之前需要先解锁交易密码）

# trd_ctx.close()  # 关闭对象，防止连接条数用尽APP

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
