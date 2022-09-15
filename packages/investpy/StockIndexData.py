import investpy
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドindexDataFromToday
引数index : ティッカー
引数period : データの期間（年）
'''


def indexDataFromToday(index, period):
    end = date.today().strftime('%d/%m/%Y')
    start = (date.today() - relativedelta(years=period)).strftime('%d/%m/%Y')
    # print(f"{ticker}・期間：{start}〜{end}")
    df = investpy.get_index_historical_data(index=index,
                                            country='United States',
                                            from_date=start,
                                            to_date=end)
    return df


'''
メソッドindexDataFromDD(designated day)
引数index : ティッカー
引数period : データの期間（年）
引数d_start : データの最終日
'''


def indexDataFromDD(index, period, d_start):
    end = d_start.strftime('%d/%m/%Y')
    start = (d_start - relativedelta(years=period)).strftime('%d/%m/%Y')
    # print(f"{ticker}・期間：{start}〜{end}")
    df = investpy.get_index_historical_data(index=index,
                                            country='United States',
                                            from_date=start,
                                            to_date=end)
    return df
