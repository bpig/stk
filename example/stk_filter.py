import pandas as pd
from util import *
from futu import *
import time

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
simple_filter = SimpleFilter()
simple_filter.filter_min = 2
simple_filter.filter_max = 1000
simple_filter.stock_field = StockField.CUR_PRICE
simple_filter.is_no_filter = False
# simple_filter.sort = SortDir.ASCEND

financial_filter = FinancialFilter()
financial_filter.filter_min = 0.5
financial_filter.filter_max = 50
financial_filter.stock_field = StockField.CURRENT_RATIO
financial_filter.is_no_filter = False
financial_filter.sort = SortDir.ASCEND
financial_filter.quarter = FinancialQuarter.ANNUAL

custom_filter = CustomIndicatorFilter()
custom_filter.ktype = KLType.K_DAY
custom_filter.stock_field1 = StockField.MA10
custom_filter.stock_field2 = StockField.MA60
custom_filter.relative_position = RelativePosition.MORE
custom_filter.is_no_filter = False

nBegin = 0
last_page = False
ret_list = list()
ret = None
while not last_page:
    nBegin += len(ret_list)
    ret, ls = quote_ctx.get_stock_filter(
        market=Market.HK,
        filter_list=[simple_filter, financial_filter, custom_filter],
        begin=nBegin)  # 对香港市场的股票做简单、财务和指标筛选
    if ret == RET_OK:
        last_page, all_count, ret_list = ls
        print('all count = ', all_count)

        # dd = pd.concat(ret_list)
        # if not ret:
        #     ret = pd.concat([ret, dd])
        # else:
        #     ret = dd
        for item in ret_list:
            print(item.stock_code)  # 取股票代码
            print(item.stock_name)  # 取股票名称
            print(item[simple_filter])  # 取 simple_filter 对应的变量值
            print(item.cur_price)  # 效果同上，也是取 simple_filter 对应的变量值
            print(item[financial_filter])  # 取 financial_filter 对应的变量值
            print(item[custom_filter])  # 获取 custom_filter 的数值
    else:
        print('error: ', ls)
    time.sleep(3)  # 加入时间间隔，避免触发限频
ret.to_pickle("select.df")

quote_ctx.close()
