from pandas_datareader import data
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドstockDataFormToday
引数ticker : ティッカー
引数period : データの期間（年）
'''


def stockDataFromToday(ticker, period):
	end = date.today().strftime('%d/%m/%Y')
	start = (date.today() - relativedelta(years=period)).strftime('%d/%m/%Y')
	# print(f"{ticker}・期間：{start}〜{end}")
	df = data.DataReader(ticker, "yahoo", start, end)
	return df


'''
メソッドstockDataFormDD(designated day)
引数ticker : ティッカー
引数period : データの期間（年）
引数d_start : データの最終日
'''


def stockDataFromDD(ticker, period, d_start):
	end = d_start
	start = (d_start - relativedelta(years=period))
	# print(f"{ticker}・期間：{start}〜{end}")
	df = data.DataReader(ticker, "yahoo", start, end)
	return df

