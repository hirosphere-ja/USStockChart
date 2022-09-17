import pandas as pd
from pandas_datareader import data
from dateutil.relativedelta import relativedelta
from datetime import date

'''
メソッドstockDataFormToday
引数ticker : ティッカー
引数period : データの期間（年）
'''


def stockDataFromToday(ticker, period):
	end = pd.to_datetime(date.today(), format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((date.today() - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
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
	d_start = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	end = pd.to_datetime(d_start, format='%d/%m/%Y', infer_datetime_format=True)
	start = pd.to_datetime((d_start - relativedelta(years=period)), format='%d/%m/%Y', infer_datetime_format=True)
	# print(f"{ticker}・期間：{start}〜{end}")
	df = data.DataReader(ticker, "yahoo", start, end)
	return df


